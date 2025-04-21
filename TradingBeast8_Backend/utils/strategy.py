import MetaTrader5 as mt5
import os
from dotenv import load_dotenv

load_dotenv()

def run_strategy():
    login = int(os.getenv("MT5_LOGIN"))
    password = os.getenv("MT5_PASSWORD")
    server = os.getenv("MT5_SERVER")
    mt5.initialize(login=login, password=password, server=server)
    
    account_info = mt5.account_info()
    print("Logged in:", account_info.name)

    # Here you'd add sniper logic (simplified example)
    print("Running strategy... (mock logic)")

    mt5.shutdown()