import asyncio
from pyrogram import Client

async def generate():
    print("--- Pyrogram String Session Generator ---")
    api_id = input("API_ID'nizi girin: ").strip()
    if not api_id.isdigit():
        print("Hata: API_ID sadece rakamlardan oluşmalıdır.")
        return
    api_id = int(api_id)
    api_hash = input("API_HASH'inizi girin: ").strip()
    
    print("\n[Bilgi] Telegram şimdi telefon numaranızı ve ardından gelen doğrulama kodunu isteyecek.")
    print("[Önemli] Telefon numarasını ülke koduyla birlikte girin (Örn: +905xxxxxxxxx)\n")
    
    async with Client("session_temp", api_id=api_id, api_hash=api_hash, in_memory=True) as app:
        session = await app.export_session_string()
        print("\n" + "="*50)
        print("🎉 STRING SESSION BAŞARIYLA OLUŞTURULDU! 🎉")
        print("="*50)
        print(session)
        print("="*50)
        print("[İpucu] Yukarıdaki uzun kodu kopyalayıp .env dosyanızdaki STRING_SESSION kısmına yapıştırın.")

if __name__ == "__main__":
    try:
        asyncio.run(generate())
    except KeyboardInterrupt:
        print("\nİşlem iptal edildi.")
    except Exception as e:
        print(f"\nHata oluştu: {e}")
