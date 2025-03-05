import os
import httpx

from dotenv import load_dotenv

load_dotenv(os.path.join('..', 'config', '.env'))
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")

def request_template():
    headers = {
        'Accept': "application/json",
        'Authorization': f"Bearer {ACCESS_TOKEN}"
    }
    response = httpx.get("https://api.surveymonkey.com/v3/users/me", headers=headers)
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error: {response.status_code} - {response.text}")


## ----------------------------------- Call the functions pulling data --------------------------------------------------------------------------------------------------------
get_me()