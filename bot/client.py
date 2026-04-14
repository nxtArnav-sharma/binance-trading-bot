import os
from binance.client import Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

TESTNET_URL = "https://testnet.binancefuture.com"

def get_client():
    client = Client(API_KEY, API_SECRET)

    # switch to futures testnet
    client.FUTURES_URL = TESTNET_URL + "/fapi"

    return client