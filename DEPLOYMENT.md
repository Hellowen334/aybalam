# Rose X Music Deployment Guide for Ubuntu Server

This guide explains how to deploy, configure, and manage your private version of **Rose X Music Bot** on an Ubuntu VPS.

---

## 📋 Table of Contents
1. [Prerequisites](#1-prerequisites)
2. [Setup the Environment](#2-setup-the-environment)
3. [Configuration (.env)](#3-configuration-env)
4. [Systemd Service Setup (Recommended)](#4-systemd-service-setup-recommended)
5. [Monitoring & Logs](#5-monitoring--logs)

---

## 1. Prerequisites

Run the following commands on your Ubuntu server to update packages and install system dependencies:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3-pip python3-venv ffmpeg nodejs npm git
```

---

## 2. Setup the Environment

We recommend running the bot in a Python virtual environment to isolate dependencies:

1. **Clone/Move the Bot files** to your server:
   ```bash
   # Move/clone your project files to:
   /home/ubuntu/music
   ```

2. **Navigate to the bot directory**:
   ```bash
   cd /home/ubuntu/music
   ```

3. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   ```

4. **Activate the virtual environment & install requirements**:
   ```bash
   source venv/bin/activate
   pip install -U pip
   pip install -r requirements.txt
   ```

---

## 3. Configuration (.env)

Create a copy of `sample.env` named `.env` and fill in your details:

```bash
cp sample.env .env
nano .env
```

### Essential Variables:
* **API_ID** & **API_HASH**: Get them from [my.telegram.org](https://my.telegram.org)
* **BOT_TOKEN**: Create a bot with [@BotFather](https://t.me/BotFather) and paste the token.
* **OWNER_ID**: Your Telegram user ID (required for administrative and security verification).
* **MONGO_DB_URI**: A MongoDB database URI (e.g., from MongoDB Atlas or local MongoDB instance).
* **LOGGER_ID**: Telegram channel/group ID (with minus sign, e.g. `-100xxxxxxx`) where the bot logs play activities.
* **STRING_SESSION**: Pyrogram String Session for the assistant user account (generated using your Pyrogram helper script).

---

## 4. Systemd Service Setup (Recommended)

To run the bot in the background, auto-start on boot, and auto-restart on crashes:

1. **Copy the template service file** to systemd folder:
   ```bash
   sudo cp music_bot.service.example /etc/systemd/system/music_bot.service
   ```

2. **Edit the systemd service file** to match your server details (user, path):
   ```bash
   sudo nano /etc/systemd/system/music_bot.service
   ```
   Ensure the following lines point to correct paths:
   * `User=ubuntu` (or your user username)
   * `WorkingDirectory=/home/ubuntu/music`
   * `ExecStart=/home/ubuntu/music/venv/bin/python run.py`

3. **Reload systemd daemon, enable, and start the service**:
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable music_bot.service
   sudo systemctl start music_bot.service
   ```

---

## 5. Monitoring & Logs

* **Check the status of your bot**:
  ```bash
  sudo systemctl status music_bot.service
  ```

* **View live logs**:
  ```bash
  sudo journalctl -u music_bot.service -f
  ```

* **Restart the bot**:
  ```bash
  sudo systemctl restart music_bot.service
  ```

* **Stop the bot**:
  ```bash
  sudo systemctl stop music_bot.service
  ```
