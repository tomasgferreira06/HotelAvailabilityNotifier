# HotelAvailabilityNotifier

A simple Python script that monitors room availability on the Masa Hotel booking website and sends a Telegram notification when rooms become available.

## 🔧 Features

- Periodically checks a specific hotel booking page.
- Sends Telegram notifications when availability is detected.
- Keeps your Telegram bot credentials safe via environment variables.

## 🧪 Requirements

- Python 3.12
- A Telegram bot (created via [@BotFather](https://t.me/BotFather))
- Your personal Telegram chat ID

## 🚀 Setup Instructions

### 1. Clone this repository

```bash
git clone https://github.com/tomasgferreira06/HotelAvailabilityNotifier.git
cd HotelAvailabilityNotifier
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Copy the `.env.example` file to `.env` and replace the values:

```env
TELEGRAM_TOKEN=your_bot_token_here
CHAT_ID=your_chat_id_here
```

> Never share your `.env` file or commit it to version control. It's excluded via `.gitignore`.

## ▶️ Running the script

```bash
python main.py
```

The script will check for room availability every 1 minute. If rooms are found, you’ll receive a Telegram message like:

```
🏨 Rooms are now available at Masa Hotel! Check it here: https://book.omnibees.com/hotelresults?...
```

## 📬 How to Get Your Telegram Bot Token and Chat ID

1. Talk to [@BotFather](https://t.me/BotFather) and create a new bot.
2. Copy the token it gives you.
3. Send any message to your new bot.
4. Go to:  
   `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`
5. Look for the `"chat":{"id":...}` field — that's your `CHAT_ID`.

## 📁 Project Structure

```
HotelAvailabilityNotifier/
├── main.py              # The main script
├── .env.example         # Template for your environment variables
├── .gitignore           # Ensures sensitive files are not committed
├── requirements.txt     # Dependencies list
└── README.md            # This file
```

## 🔐 Security Advice

- Do **not** hardcode API keys or tokens.
- Always use environment variables for sensitive data.
- Rotate your Telegram bot token if it is ever exposed.

---

Made with ❤️ by a future senior developer (I hope so).
