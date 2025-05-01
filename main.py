import requests
from bs4 import BeautifulSoup
from telegram import Bot
import time
import os
from dotenv import load_dotenv


load_dotenv()


URL = 'https://book.omnibees.com/hotelresults?q=17958&lang=en-US&currencyId=34&hotel_folder=&mysite=ob&CheckIn=17052025&CheckOut=18052025&ad=3&ch=0&ag=&child_age_input=&Code=&_gl=1*1wppcgf*_gcl_au*MTM5MzQ2NjQ4Ni4xNzQ2MDM3OTky'
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
FREQUENCY_MINUTES = 10

def check_availability():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()


    if "We did not find availability for the selected period" not in text:
        bot = Bot(token=TELEGRAM_TOKEN)
        bot.send_message(chat_id=CHAT_ID, text=f"🏨 Rooms are now available at Masa Hotel! Check it now: {URL}")
        return True
    return False

if __name__ == "__main__":
    while True:
        print("🔍 Checking availability...")
        try:
            if check_availability():
                print("✅ Rooms found! Notification sent.")
            else:
                print("❌ No availability yet.")
        except Exception as e:
            print(f"⚠️ Error while checking: {e}")

        time.sleep(FREQUENCY_MINUTES * 60)
