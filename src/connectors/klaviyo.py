import os

from typing import Any
from typing import List
from typing import Optional
from dotenv import load_dotenv
from klaviyo_api import KlaviyoAPI

# Loading api token from config dir
load_dotenv("./src/config/.env")
API_KEY_KLAVIYO = os.environ.get("API_KEY_KLAVIYO")

klaviyo = KlaviyoAPI(API_KEY_KLAVIYO, max_delay = 60, max_retries = 3, test_host = None)  

def get_profiles(
        additional_fields_profile: List[str], 
        fields_profile: List[str], 
        filter: str,
        page_cursor: str, 
        page_size: int, 
        sort: str
) -> Optional[dict]:
    """Send a request to retrieve a list of profiles.

    This function constructs a request to retrieve all profiles available in the Klaviyo account. 

    Args:
        additional_fields_profile (List[str]): A comma-separated list of additional fields to include in the profile data (e.g., 'predictive_analytics').
        fields_profile (List[str]): A comma-separated list of fields to retrieve for each profile. (e.g., 'first_name', 'location')
        filter (str): A filter to apply to the profiles being retrieved.
        page_cursor (str): A cursor for pagination to retrieve the next set of results.
        page_size (int): The number of profiles to retrieve per page.
        sort (str): The sorting order for the profiles (e.g., by creation date).

    Returns:
        Optional[dict]: A dictionary containing the profile data, or an error message if an exception occurs.
    """
    try:
        response = klaviyo.Profiles.get_profiles(
            additional_fields_profile=additional_fields_profile, 
            fields_profile=fields_profile, 
            filter=filter, 
            page_cursor=page_cursor, 
            page_size=page_size, 
            sort=sort
        )
        return response
    
    except Exception as e:
        return f"The following exception occurred:{e}"

##------------------------------------------------------ Call the functions to pull the data--------------------------------------------

profiles = get_profiles(
    additional_fields_profile = ['predictive_analytics'],
    fields_profile = ['first_name', 'location'],
    filter = 1,
    page_cursor = None,
    page_size = 20,
    sort = 'created'
)

print(profiles)

