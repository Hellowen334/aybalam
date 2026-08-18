# -----------------------------------------------
# 🔸 Aybalam Music Project
# 🔹 Developed & Maintained by: Aybalam Music (https://t.me/aryaduyuru)
# 📅 Copyright © 2022 – All Rights Reserved
# -----------------------------------------------
import asyncio
import sys
from SHUKLAMUSIC.logging import LOGGER
from apscheduler.schedulers.asyncio import AsyncIOScheduler

async def update_ytdlp():
    LOGGER("yt-dlp").info("Checking for yt-dlp nightly/pre-release updates...")
    try:
        proc = await asyncio.create_subprocess_exec(
            sys.executable, "-m", "pip", "install", "-U", "--pre", "yt-dlp",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await proc.communicate()
        if proc.returncode == 0:
            LOGGER("yt-dlp").info("yt-dlp updated successfully.")
            # Verify and log version
            ver_proc = await asyncio.create_subprocess_exec(
                "yt-dlp", "--version",
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            v_stdout, _ = await ver_proc.communicate()
            version = v_stdout.decode().strip()
            LOGGER("yt-dlp").info(f"Current yt-dlp version: {version}")
        else:
            LOGGER("yt-dlp").error(f"Failed to update yt-dlp: {stderr.decode()}")
    except Exception as e:
        LOGGER("yt-dlp").error(f"Error during yt-dlp update: {e}")

def start_ytdlp_updater_scheduler():
    # Run once on startup asynchronously
    asyncio.create_task(update_ytdlp())
    # Schedule to run every 24 hours
    scheduler = AsyncIOScheduler()
    scheduler.add_job(update_ytdlp, trigger="interval", hours=24)
    scheduler.start()
    LOGGER("yt-dlp").info("yt-dlp nightly updater scheduler started (runs every 24 hours).")
