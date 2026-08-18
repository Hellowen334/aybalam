# -----------------------------------------------
# 🔸 Aybalam Music Project
# 🔹 Developed & Maintained by: Aybalam Music (https://t.me/aryaduyuru)
# 📅 Copyright © 2022 – All Rights Reserved
#
# 📖 License:
# This source code is open for educational and non-commercial use ONLY.
# You are required to retain this credit in all copies or substantial portions of this file.
# Commercial use, redistribution, or removal of this notice is strictly prohibited
# without prior written permission from the author.
#
# ❤️ Made with ❤️ for Aybalam Music Community
# -----------------------------------------------
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)
from SHUKLAMUSIC import YouTube, app
from SHUKLAMUSIC.utils.database import (
    add_playlist,
    delete_playlist,
    get_playlist_names,
    remove_playlist,
)
from SHUKLAMUSIC.utils.decorators import language, languageCB
from config import BANNED_USERS

@app.on_message(
    filters.command(
        ["playlist", "playlists", "myplaylist", "myplaylists"],
        prefixes=["/", "!", "%", ",", "", ".", "@", "#"]
    ) & ~BANNED_USERS
)
@language
async def playlist_(client, message: Message, _):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    playlist = await get_playlist_names(user_id)
    if not playlist:
        return await message.reply_text(
            "⭐ **Kişisel Çalma Listeniz Boş! / Your Personal Playlist is Empty!**\n\n"
            "Şarkı eklemek için / To add songs:\n"
            "• `/addplaylist <şarkı adı veya link / song name or link>`\n"
            "• Veya çalan şarkıdaki **⭐ Add to Playlist** butonuna tıklayın."
        )
    
    msg = f"⭐ **{user_name}'s Personal Playlist**\n\n"
    for i, track in enumerate(playlist, start=1):
        msg += f"{i}. **{track['title'][:35]}** ({track['duration']})\n"
    
    buttons = []
    if message.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
        buttons.append([
            InlineKeyboardButton("🎵 Play Audio", callback_data=f"play_personal_playlist|a|{message.chat.id}"),
            InlineKeyboardButton("🎬 Play Video", callback_data=f"play_personal_playlist|v|{message.chat.id}")
        ])
    else:
        buttons.append([
            InlineKeyboardButton("📱 Play in Group", switch_inline_query_current_chat="")
        ])
    buttons.append([
        InlineKeyboardButton("🗑 Clear Playlist", callback_data="clear_personal_playlist"),
        InlineKeyboardButton("❌ Close", callback_data="close")
    ])
    
    await message.reply_text(
        msg,
        reply_markup=InlineKeyboardMarkup(buttons)
    )

@app.on_message(
    filters.command(
        ["addplaylist"],
        prefixes=["/", "!", "%", ",", "", ".", "@", "#"]
    ) & ~BANNED_USERS
)
@language
async def addplaylist_(client, message: Message, _):
    if len(message.command) < 2:
        if message.reply_to_message:
            query = message.reply_to_message.text or message.reply_to_message.caption
        else:
            return await message.reply_text(
                "⭐ **Usage / Kullanım:**\n"
                "• `/addplaylist <şarkı adı veya link / song name or link>`\n"
                "• Veya bir mesaja yanıt vererek `/addplaylist` yazın."
            )
    else:
        query = message.text.split(None, 1)[1]
    
    mystic = await message.reply_text("🔎 **YouTube'da aranıyor... / Searching YouTube...**")
    try:
        title, duration_min, duration_sec, thumbnail, vidid = await YouTube.details(query)
    except Exception:
        return await mystic.edit_text("❌ **Şarkı bulunamadı! / No song found!**")
    
    user_id = message.from_user.id
    added = await add_playlist(user_id, vidid, title, duration_min)
    if added:
        await mystic.edit_text(
            f"⭐ **Çalma Listesine Eklendi! / Added to Playlist!**\n\n"
            f"• **Title:** {title}\n"
            f"• **Duration:** {duration_min}"
        )
    else:
        await mystic.edit_text("⚠️ **Bu şarkı zaten çalma listenizde var! / This song is already in your playlist!**")

@app.on_message(
    filters.command(
        ["delplaylist", "removeplaylist"],
        prefixes=["/", "!", "%", ",", "", ".", "@", "#"]
    ) & ~BANNED_USERS
)
@language
async def delplaylist_(client, message: Message, _):
    if len(message.command) < 2:
        return await message.reply_text(
            "⭐ **Usage / Kullanım:**\n"
            "• `/delplaylist <sıra numarası / track number>` (örn: `/delplaylist 3`)\n"
            "• `/delplaylist <şarkı adı / song name>`"
        )
    
    user_id = message.from_user.id
    query = message.text.split(None, 1)[1].strip()
    
    playlist = await get_playlist_names(user_id)
    if not playlist:
        return await message.reply_text("❌ **Çalma listeniz boş! / Your playlist is empty!**")
        
    if query.isdigit():
        idx = int(query) - 1
        if idx < 0 or idx >= len(playlist):
            return await message.reply_text("❌ **Geçersiz sıra numarası! / Invalid track number!**")
        song = playlist[idx]
        await remove_playlist(user_id, song["videoid"])
        return await message.reply_text(f"🗑 **Çalma listesinden silindi / Removed from playlist:** {song['title']}")
        
    for song in playlist:
        if query.lower() in song["title"].lower() or query == song["videoid"]:
            await remove_playlist(user_id, song["videoid"])
            return await message.reply_text(f"🗑 **Çalma listesinden silindi / Removed from playlist:** {song['title']}")
            
    try:
        _, _, _, _, vidid = await YouTube.details(query)
        for song in playlist:
            if song["videoid"] == vidid:
                await remove_playlist(user_id, vidid)
                return await message.reply_text(f"🗑 **Çalma listesinden silindi / Removed from playlist:** {song['title']}")
    except:
        pass
        
    await message.reply_text("❌ **Çalma listenizde eşleşen şarkı bulunamadı! / No matching song found!**")

@app.on_callback_query(filters.regex(r"^add_to_playlist\s+(.+)$") & ~BANNED_USERS)
async def add_to_playlist_cb(client, callback_query: CallbackQuery):
    videoid = callback_query.data.split(None, 1)[1]
    user_id = callback_query.from_user.id
    
    try:
        title, duration_min, duration_sec, thumbnail, vidid = await YouTube.details(videoid, videoid=True)
    except Exception:
        return await callback_query.answer("Şarkı detayları alınamadı! / Failed to retrieve song details!", show_alert=True)
    
    added = await add_playlist(user_id, vidid, title, duration_min)
    if added:
        await callback_query.answer(f"Added to playlist: {title[:40]}...", show_alert=True)
    else:
        await callback_query.answer("This song is already in your playlist!", show_alert=True)

@app.on_callback_query(filters.regex(r"^play_personal_playlist\|") & ~BANNED_USERS)
@languageCB
async def play_personal_playlist_cb(client, callback_query: CallbackQuery, _):
    data = callback_query.data.split("|")
    mode = data[1]
    chat_id = int(data[2])
    user_id = callback_query.from_user.id
    user_name = callback_query.from_user.first_name
    
    playlist = await get_playlist_names(user_id)
    if not playlist:
        return await callback_query.answer("Your playlist is empty!", show_alert=True)
    
    await callback_query.message.delete()
    mystic = await callback_query.message.reply_text(_["play_1"])
    
    result = [track["videoid"] for track in playlist]
    video = True if mode == "v" else None
    
    from SHUKLAMUSIC.utils.stream.stream import stream
    try:
        await stream(
            _,
            mystic,
            user_id,
            result,
            chat_id,
            user_name,
            chat_id,
            video,
            streamtype="playlist",
            spotify=False,
            forceplay=None,
        )
    except Exception as e:
        await mystic.edit_text(f"Error: {e}")

@app.on_callback_query(filters.regex("^clear_personal_playlist$") & ~BANNED_USERS)
async def clear_playlist_cb(client, callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    playlist = await get_playlist_names(user_id)
    if not playlist:
        return await callback_query.answer("Your playlist is already empty!", show_alert=True)
    
    buttons = [
        [
            InlineKeyboardButton("✅ Confirm Clear", callback_data="confirm_clear_personal_playlist"),
            InlineKeyboardButton("❌ Cancel", callback_data="playlist_menu")
        ]
    ]
    await callback_query.message.edit_text(
        "⚠️ **Kişisel çalma listenizi temizlemek istediğinizden emin misiniz? / Are you sure you want to clear your playlist?**",
        reply_markup=InlineKeyboardMarkup(buttons)
    )

@app.on_callback_query(filters.regex("^confirm_clear_personal_playlist$") & ~BANNED_USERS)
async def confirm_clear_playlist_cb(client, callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    await delete_playlist(user_id)
    await callback_query.answer("Successfully cleared your playlist!", show_alert=True)
    await callback_query.message.edit_text(
        "⭐ **Kişisel çalma listeniz temizlendi. / Your playlist has been cleared.**"
    )

@app.on_callback_query(filters.regex("^playlist_menu$") & ~BANNED_USERS)
async def playlist_menu_cb(client, callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    user_name = callback_query.from_user.first_name
    playlist = await get_playlist_names(user_id)
    if not playlist:
        return await callback_query.message.edit_text(
            "⭐ **Kişisel Çalma Listeniz Boş! / Your Personal Playlist is Empty!**\n\n"
            "Şarkı eklemek için / To add songs:\n"
            "• `/addplaylist <şarkı adı veya link / song name or link>`\n"
            "• Veya çalan şarkıdaki **⭐ Add to Playlist** butonuna tıklayın."
        )
    
    msg = f"⭐ **{user_name}'s Personal Playlist**\n\n"
    for i, track in enumerate(playlist, start=1):
        msg += f"{i}. **{track['title'][:35]}** ({track['duration']})\n"
        
    buttons = []
    if callback_query.message.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
        buttons.append([
            InlineKeyboardButton("🎵 Play Audio", callback_data=f"play_personal_playlist|a|{callback_query.message.chat.id}"),
            InlineKeyboardButton("🎬 Play Video", callback_data=f"play_personal_playlist|v|{callback_query.message.chat.id}")
        ])
    else:
        buttons.append([
            InlineKeyboardButton("📱 Play in Group", switch_inline_query_current_chat="")
        ])
    buttons.append([
        InlineKeyboardButton("🗑 Clear Playlist", callback_data="clear_personal_playlist"),
        InlineKeyboardButton("❌ Close", callback_data="close")
    ])
    
    await callback_query.message.edit_text(
        msg,
        reply_markup=InlineKeyboardMarkup(buttons)
    )
