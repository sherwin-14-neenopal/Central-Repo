import os

from typing import Any
from typing import Optional
from dotenv import load_dotenv
from klaviyo_api import KlaviyoAPI

# Loading api token from config dir
load_dotenv("./src/config/.env")
API_KEY_KLAVIYO = os.environ.get("API_KEY_KLAVIYO")

klaviyo = KlaviyoAPI(API_KEY_KLAVIYO, max_delay=60, max_retries=3, test_host=None)  

