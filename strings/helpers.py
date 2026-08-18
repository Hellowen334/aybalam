HELP_1 = """<b><u>ʏöɴᴇᴛɪᴄɪ ᴋᴏᴍᴜᴛʟᴀʀı :</u></b>

Kanalda kullanmak için komutların başına <b>c</b> ekleyin.

• /pause : Çalan müziği duraklatır.  
• /resume : Duraklatılan müziği devam ettirir.  
• /skip : Mevcut şarkıyı atlar ve sıradakini çalar.  
• /end ᴠᴇʏᴀ /stop : Sırayı temizler ve müziği durdurur.  
• /player : Etkileşimli oynatıcı panelini açar.  
• /queue : Sıradaki şarkıları gösterir.
"""

HELP_2 = """<b><u>ʏᴇᴛᴋɪʟɪ ᴋᴜʟʟᴀɴıᴄıʟᴀʀ :</u></b>

Yetkili kullanıcılar, grupta yönetici olmasalar bile yönetici komutlarını kullanabilirler.

• /auth [ᴋᴜʟʟᴀɴıᴄı ᴀᴅı/ɪᴅ] : Bir kullanıcıyı yetkili listesine ekler.  
• /unauth [ᴋᴜʟʟᴀɴıᴄı ᴀᴅı/ɪᴅ] : Bir kullanıcıyı yetkili listesinden çıkarır.  
• /authusers : Yetkili kullanıcıların listesini gösterir.
"""

HELP_3 = """<b><u>ᴅᴜʏᴜʀᴜ (ʙʀᴏᴀᴅᴄᴀsᴛ) :</u></b> [Sadece Sudo]

• /broadcast [ᴍᴇsᴀᴊ/ʏᴀɴıᴛ] : Hizmet verilen tüm sohbetlere duyuru gönderir.

<b>ᴍᴏᴅʟᴀʀ :</b>  
- <b>-pin</b> : Mesajı sabitler.  
- <b>-pinloud</b> : Mesajı sabitler ve bildirim gönderir.  
- <b>-user</b> : Botu başlatan kullanıcılara gönderir.  
- <b>-assistant</b> : Asistan hesabı üzerinden gönderir.  
- <b>-nobot</b> : Bot üzerinden gönderimi kapatır.

<b>öʀɴᴇᴋ :</b>  
<code>/broadcast -user -assistant -pin ᴛᴇsᴛ ᴅᴜʏᴜʀᴜsᴜ</code>
"""

HELP_4 = """<b><u>sᴏʜʙᴇᴛ ᴋᴀʀᴀ ʟɪsᴛᴇsɪ :</u></b> [Sadece Sudo]

Kötüye kullanan sohbetlerin botu kullanmasını kısıtlar.

• /blacklistchat [ɪᴅ] : Bir sohbeti kara listeye alır.  
• /whitelistchat [ɪᴅ] : Bir sohbeti kara listeden çıkarır.  
• /blacklistedchat : Kara listeye alınan tüm sohbetleri gösterir.
"""

HELP_5 = """<b><u>ᴋᴜʟʟᴀɴıᴄı ᴇɴɢᴇʟʟᴇᴍᴇ :</u></b> [Sadece Sudo]

Engellenen kullanıcılar bot komutlarını kullanamaz.

• /block [ᴋᴜʟʟᴀɴıᴄı/ʏᴀɴıᴛ] : Bir kullanıcıyı engeller.  
• /unblock [ᴋᴜʟʟᴀɴıᴄı/ʏᴀɴıᴛ] : Bir kullanıcının engelini kaldırır.  
• /blockedusers : Engellenen tüm kullanıcıları gösterir.
"""

HELP_6 = """<b><u>ᴋᴀɴᴀʟᴅᴀ ᴏʏɴᴀᴛᴍᴀ :</u></b>

Kanalda ses/video yayını yapın.

• /cplay : Ses yayınını başlatır.  
• /cvplay : Video yayınını başlatır.  
• /cplayforce ᴠᴇʏᴀ /cvplayforce : Yeni bir yayını zorla başlatır.  
• /channelplay [ᴋᴜʟʟᴀɴıᴄı ᴀᴅı/ɪᴅ] ᴠᴇʏᴀ [disable] : Bir kanalı gruba bağlar.
"""

HELP_7 = """<b><u>ɢʟᴏʙᴀʟ ʏᴀsᴀᴋ (ɢʙᴀɴ) :</u></b> [Sadece Sudo]

• /gban [ᴋᴜʟʟᴀɴıᴄı/ʏᴀɴıᴛ] : Bir kullanıcıyı botun bulunduğu tüm gruplardan yasaklar.  
• /ungban [ᴋᴜʟʟᴀɴıᴄı/ʏᴀɴıᴛ] : Küresel yasağı kaldırır.  
• /gbannedusers : Küresel yasaklı kullanıcıları gösterir.
"""

HELP_8 = """<b><u>ᴅöɴɢü (ʟᴏᴏᴘ) :</u></b>

Mevcut şarkıyı tekrarlar.

• /loop [enable/disable] : Döngüyü açar veya kapatır.  
• /loop [1–10] : Döngü sayısını ayarlar.
"""

HELP_9 = """<b><u>ʙᴀᴋıᴍ (ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ) :</u></b> [Sadece Sudo]

• /logs : Bot kayıtlarını (log) alır.  
• /logger [enable/disable] : Etkinlik kaydını açar veya kapatır.  
• /maintenance [enable/disable] : Bakım modunu açar veya kapatır.
"""

HELP_10 = """<b><u>ᴘɪɴɢ ᴠᴇ ɪsᴛᴀᴛɪsᴛɪᴋʟᴇʀ :</u></b>

• /start : Botu başlatır.  
• /help : Yardım menüsünü gösterir.  
• /ping : Botun gecikme süresini ve sistem istatistiklerini gösterir.  
• /stats : Genel bot istatistiklerini gösterir.
"""

HELP_11 = """<b><u>ᴏʏɴᴀᴛᴍᴀ ᴋᴏᴍᴜᴛʟᴀʀı :</u></b>

<b>v :</b> Video oynatır.  
<b>force :</b> Zorla oynatır (sırayı atlar).  

• /play ᴠᴇʏᴀ /vplay : Ses/video yayınını başlatır.  
• /playforce ᴠᴇʏᴀ /vplayforce : Yeni bir yayını zorla başlatır.
"""

HELP_12 = """<b><u>sıʀᴀʏı ᴋᴀʀışᴛıʀ (sʜᴜғғʟᴇ) :</u></b>

• /shuffle : Sıradaki şarkıları karıştırır.  
• /queue : Karıştırılmış sırayı gösterir.
"""

HELP_13 = """<b><u>sᴀʀᴅıʀᴍᴀ (sᴇᴇᴋ) :</u></b>

• /seek [sᴀɴɪʏᴇ] : Şarkıyı ileri sarar.  
• /seekback [sᴀɴɪʏᴇ] : Şarkıyı geri sarar.
"""

HELP_14 = """<b><u>şᴀʀᴋı ɪɴᴅɪʀᴍᴇ :</u></b>

• /song [ᴀᴅ/ʏᴛ ʟɪɴᴋɪ] : Bir şarkıyı MP3 veya MP4 formatında indirir.
"""

HELP_15 = """<b><u>ʜıᴢ ᴋᴏᴍᴜᴛʟᴀʀı :</u></b> [Sadece Yönetici]

Yayın oynatma hızını kontrol edin.

• /speed ᴠᴇʏᴀ /playback : Gruplarda ses hızını ayarlar.  
• /cspeed ᴠᴇʏᴀ /cplayback : Kanallarda ses hızını ayarlar.
"""

HELP_16 = """<b><u>sᴏʜʙᴇᴛ ᴏʏᴜɴʟᴀʀı :</u></b>

Kelime, emoji ve bayrak tahmin etme oyunları.

• /wordgame ᴠᴇʏᴀ /cfword : Kelime tahmin oyunu başlatır.
• /emojigame ᴠᴇʏᴀ /cfemoji : Emoji tahmin oyunu başlatır.
• /flaggame ᴠᴇʏᴀ /cfflag : Bayrak tahmin oyunu başlatır.
• /wordleaderboard ᴠᴇʏᴀ /gametop ᴠᴇʏᴀ /cflb : Küresel liderlik tablosunu gösterir.
"""

HELP_17 = """<b><u>ɢɪᴛʜᴜʙ ʏöɴᴇᴛɪᴍɪ :</u></b>

GitHub repolarınızı yönetin.

• /setghtoken [token] : GitHub token'ınızı kaydeder (Sadece DM).
• /myrepos : Repolarınızı listeler.
• /creategh [name] : Yeni repo oluşturur.
"""

HELP_18 = """<b><u>sᴏʜʙᴇᴛ ʙᴏᴛᴜ (ᴄʜᴀᴛʙᴏᴛ) :</u></b>

Otomatik yanıt sistemi.

• /chatbot on/off : Otomatik yanıtı açar/kapatır (Yönetici).
• /teach [kelime] | [yanıt] : Bota yeni bir yanıt öğretir.
• /unlearn [kelime] : Öğretilen bir yanıtı siler.
"""

HELP_19 = """🎮 <b><u>ɢʀᴜᴘ ᴏʏᴜɴʟᴀʀı :</u></b>

• /dicebattle — Zar savaşı başlatır.
• /numberbomb — Sayı bombası oyunu.
• /roulette — Rus ruleti.
• /triviabattle — Bilgi yarışması.
"""

HELP_20 = """🔑 <b><u>sᴇssɪᴏɴ sᴛʀɪɴɢ ᴏʟᴜşᴛᴜʀᴜᴄᴜ :</u></b>

• /genstring — Etkileşimli session string oluşturucuyu başlatır.
"""

HELP_21 = """⚡ <b><u>ʜıᴢʟı ɢʀᴜᴘ ᴏʏᴜɴʟᴀʀı :</u></b>

• /taprace — Butona ilk basan kazanır.
• /slots — Slot makinesini çevirir.
• /hotvote — Grup oylaması başlatır.
"""

HELP_22 = """⚔️ <b><u>ʏᴀsᴀᴋʟᴀᴍᴀ ᴠᴇ ᴍᴏᴅᴇʀᴀsʏᴏɴ :</u></b>

• /ban [ᴋᴜʟʟᴀɴıᴄı/ʏᴀɴıᴛ] — Kullanıcıyı gruptan yasaklar.
• /unban [ᴋᴜʟʟᴀɴıᴄı/ʏᴀɴıᴛ] — Yasağı kaldırır.
• /mute [ᴋᴜʟʟᴀɴıᴄı/ʏᴀɴıᴛ] — Kullanıcıyı susturur.
• /unmute [ᴋᴜʟʟᴀɴıᴄı/ʏᴀɴıᴛ] — Susturmayı kaldırır.
• /kick [ᴋᴜʟʟᴀɴıᴄı/ʏᴀɴıᴛ] — Kullanıcıyı gruptan atar.
• /promote [ᴋᴜʟʟᴀɴıᴄı/ʏᴀɴıᴛ] — Kullanıcıyı yönetici yapar.
• /demote [ᴋᴜʟʟᴀɴıᴄı/ʏᴀɴıᴛ] — Yöneticiliği alır.
• /warn [ᴋᴜʟʟᴀɴıᴄı/ʏᴀɴıᴛ] — Kullanıcıyı uyarır (3 uyarı = ban).
"""

HELP_23 = """📌 <b><u>ᴇᴛɪᴋᴇᴛ ᴋᴏᴍᴜᴛʟᴀʀı :</u></b>

• /tagall ᴠᴇʏᴀ /all — Gruptaki herkesi etiketler.
• /admintag ᴠᴇʏᴀ /admins — Tüm yöneticileri etiketler.
• /cancel ᴠᴇʏᴀ /histop — Devam eden etiketleme işlemini durdurur.
"""

HELP_24 = """👋 <b><u>ᴋᴀʀşıʟᴀᴍᴀ ᴠᴇ ɢᴇᴄᴇ ᴍᴏᴅᴜ :</u></b>

<b>ᴋᴀʀşıʟᴀᴍᴀ :</b>
• /welcome on — Karşılama mesajını açar.
• /welcome off — Karşılama mesajını kapatır.
• /welcome [ᴍᴇsᴀᴊ] — Özel bir karşılama mesajı ayarlar.

<b>ɢᴇᴄᴇ ᴍᴏᴅᴜ :</b>
• /nightmode on — Gece modunu açar.
"""

HELP_25 = """💑 <b><u>ɢüɴüɴ çɪғᴛɪ :</u></b>

• /couple — Günün çiftini seçer ❤️
• /couples — Günün çiftini fotoğraflı şekilde gösterir 🖼️
"""

HELP_26 = """ℹ️ <b><u>ᴋᴜʟʟᴀɴıᴄı ʙɪʟɢɪsɪ :</u></b>

• /info [ᴋᴜʟʟᴀɴıᴄı/ʏᴀɴıᴛ] — Kullanıcı hakkında detaylı bilgi gösterir.
• /id — Sizin veya sohbetin ID'sini gösterir.
"""

HELP_27 = """⚡ <b><u>ᴅᴏğʀᴜʟᴜᴋ ᴠᴇ ᴄᴇsᴀʀᴇᴛ :</u></b>

• /truth — Rastgele bir doğruluk sorusu sorar.
• /dare — Rastgele bir cesaret görevi verir.
"""

HELP_28 = """📋 <b><u>ɴᴏᴛʟᴀʀ ᴠᴇ ғɪʟᴛʀᴇʟᴇʀ :</u></b>

<b>ɴᴏᴛʟᴀʀ :</b>
• /save [ᴀᴅ] [ɪçᴇʀɪᴋ/ʏᴀɴıᴛ] — Bir not kaydeder.
• /get [ᴀᴅ] ᴠᴇʏᴀ #ᴀᴅ — Kaydedilmiş bir notu getirir.
• /notes — Tüm notları listeler.
• /clear [ᴀᴅ] — Bir notu siler.

<b>ғɪʟᴛʀᴇʟᴇʀ :</b>
• /filter [ᴋᴇʟɪᴍᴇ] [ʏᴀɴıᴛ] — Otomatik bir yanıt filtresi ayarlar.
• /stopfilter [ᴋᴇʟɪᴍᴇ] — Filtreyi siler.
"""

HELP_29 = """💤 <b><u>ᴀғᴋ (ᴜᴢᴀᴋᴛᴀ) :</u></b>

• /afk [sᴇʙᴇᴘ] — Sizi AFK (Uzaktayım) olarak işaretler. Sizi etiketleyenlere bot otomatik cevap verir.
"""

HELP_30 = """💰 <b><u>ᴋʀɪᴘᴛᴏ ᴠᴇ ᴜᴘɪ :</u></b>

• /ton — Canlı TON fiyatını gösterir.
• /usdt — Canlı USDT fiyatını gösterir.
"""

HELP_31 = """🔊 <b><u>sᴇsʟɪ sᴏʜʙᴇᴛ ʟᴏɢʟᴀʀı (ᴠᴄ ʟᴏɢɢᴇʀ) :</u></b>

Sesli sohbete katılma/ayrılma etkinliklerini belirlediğiniz bir gruba kaydeder.

• /vclogger on — Sesli sohbet loglarını açar.
• /vclogger off — Sesli sohbet loglarını kapatır.
• /vclogger set [sᴏʜʙᴇᴛ-ɪᴅ] — Logların gönderileceği hedef sohbeti ayarlar.
"""

HELP_32 = """📢 <b><u>ᴢᴏʀᴜɴʟᴜ ᴀʙᴏɴᴇʟɪᴋ (ғsᴜʙ) :</u></b>

Bot komutlarını kullanmadan önce kullanıcıların bir kanala katılmasını zorunlu kılar.

• /fsub @kanal_adi — Zorunlu kanalı ayarlar.
• /fsub off — Zorunlu aboneliği kapatır.
"""

HELP_33 = """🔔 <b><u>ᴏᴛᴏᴍᴀᴛɪᴋ ᴏɴᴀʏ :</u></b>

Gruba katılma isteklerini otomatik onaylar.

• /autoapprove on — Otomatik onayı açar.
• /autoapprove off — Otomatik onayı kapatır.
"""

HELP_34 = """🛡️ <b><u>ɢᴜᴀʀᴅɪᴀɴ — ᴀɴᴛɪ sᴘᴀᴍ :</u></b>

Grubunuzu spam mesajlara karşı korur.

• /guardian on — Korumayı açar.
• /guardian off — Korumayı kapatır.
"""

HELP_35 = """❤️ <b><u>ᴅᴜʏɢᴜʟᴀʀ ᴠᴇ ᴛᴇᴘᴋɪʟᴇʀ :</u></b>

Kullanıcılara anime GIF'leriyle duygularınızı ifade edin!

• /hug, /pat, /slap, /kiss, /cuddle vb.
"""

HELP_36 = """👬 <b><u>ᴀɪʟᴇ ɪʟɪşᴋɪʟᴇʀɪ :</u></b>

Kullanıcılarla aile ilişkileri (kardeş vb.) kurun.

• /brother @kullanici — Kardeş olarak ekler.
"""

HELP_37 = """🔊 <b><u>ᴍᴇᴛɪɴᴅᴇɴ sᴇsᴇ (ᴛᴛs) :</u></b>

Metinleri sese dönüştürür!

• /tts [metin] — Metni grubun dilinde sese çevirir.
"""
