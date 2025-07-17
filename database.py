import os
import httpx
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_API_KEY = os.getenv("SUPABASE_API_KEY")

HEADERS = {
    "apikey": SUPABASE_API_KEY,
    "Authorization": f"Bearer {SUPABASE_API_KEY}",
    "Content-Type": "application/json"
}

async def supabase_request(method, endpoint, data=None, params=None):
    url = f"{SUPABASE_URL}/rest/v1/{endpoint}"
    async with httpx.AsyncClient() as client:
        response = await client.request(method, url, headers=HEADERS, json=data, params=params)
        response.raise_for_status()
        return response.json()


