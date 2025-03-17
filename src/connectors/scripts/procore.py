import os
import json
import httpx
import pandas as pd


from typing import Optional
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv(os.path.join("..", "..", "config", ".env"))

CLIENT_ID = os.getenv("CLIENT_ID_PROCORE")
CLIENT_SECRET = os.getenv("CLIENT_SECRET_PROCORE")
REDIRECT_URI = os.getenv('REDIRECT_URI_PROCORE')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN_PROCORE')
OAUTH_URL = os.getenv('OAUTH_URL_PROCORE')
BASE_URL = os.getenv('BASE_URL_PROCORE')

conn = Procore(
        client_id = CLIENT_ID,
        client_secret = CLIENT_SECRET,
        redirect_uri = REDIRECT_URI, 
        oauth_url = OAUTH_URL,
        base_url = BASE_URL
)

companies = conn.companies.get()
for company in companies:
    print(f"Project: {company['name']} ({company['id']})")