import os
import httpx

from dotenv import load_dotenv

load_dotenv(os.path.join('..', 'config', '.env'))

# Access the ACCESS_TOKEN
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
print("ACCESS_TOKEN:", ACCESS_TOKEN)

def get_me():
    access_token = ACCESS_TOKEN
    headers = {
        'Accept': "application/json",
        'Authorization': f"Bearer {access_token}"
    }
    response = httpx.get("https://api.surveymonkey.com/v3/users/me", headers=headers)
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error: {response.status_code} - {response.text}")


## ----------------------------------- Call the functions pulling data --------------------------------------------------------------------------------------------------------
get_me()