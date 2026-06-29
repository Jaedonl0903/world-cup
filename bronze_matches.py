import requests
import os
import logging
from dotenv import load_dotenv
import json

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

API_KEY = os.getenv("FOOTBALL_DATA_API_KEY")
BASE_URL = os.getenv("BASE_URL")

params = {
    "dateFrom": "2026-06-11",
    "dateTo": "2026-07-19"
}

headers = {
    "X-Auth-Token": API_KEY
}

try:
    r = requests.get(f"{BASE_URL}/competitions/WC/matches", headers=headers, params=params)
    r.raise_for_status()

except requests.exceptions.RequestException as e:
    logger.error("Request failed: %s", e)
    raise


data = r.json()
raw = json.dumps(data)
print(raw)
