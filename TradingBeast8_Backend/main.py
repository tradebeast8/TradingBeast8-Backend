import os
from dotenv import load_dotenv
from utils.strategy import run_strategy
from utils.telegram import send_telegram_alert

load_dotenv()

def main():
    try:
        print("Starting Trading Beast 8.0 Bot...")
        run_strategy()
    except Exception as e:
        send_telegram_alert(f"⚠️ Bot Error: {e}")

if __name__ == "__main__":
    main()