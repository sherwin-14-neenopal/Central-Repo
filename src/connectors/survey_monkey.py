import os
import httpx
import pandas as pd

from dotenv import load_dotenv

## Loading access token from config dir

load_dotenv(os.path.join('..', 'config', '.env'))
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")

def request_template(endpoint):
    """Send a GET request to the specified API endpoint.

    This function constructs a request to the specified API endpoint
    using the provided Bearer token for authorization. It prints the
    response data if the request is successful, or an error message
    if the request fails.

    Args:
        endpoint (str): The API endpoint to which the request is sent.
        access_token (str): The Bearer token used for authorization.

    Returns:
        None: The function prints the response data if the request is
        successful (status code 200), otherwise it prints an error message.
    """
    headers = {
        'Accept': "application/json",
        'Authorization': f"Bearer {ACCESS_TOKEN}"
    }
    response = httpx.get(endpoint, headers=headers)
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error: {response.status_code} - {response.text}")

def get_surveys():
    endpoint = f"https://api.surveymonkey.com/v3/surveys"
    result = request_template(endpoint)
    return result


def get_survey_info(survey_id):
    endpoint = f"https://api.surveymonkey.com/v3/surveys/{survey_id}"
    result = request_template(endpoint)
    return result

def get_survey_details(survey_id):
    """Fetch detailed information about a specific survey from the SurveyMonkey API.

    This function constructs a request to the SurveyMonkey API to retrieve
    detailed information about a survey, including its pages and questions.
    It calls the `request_template` function to handle the API request and
    response.

    Args:
        survey_id (str): The ID of the survey for which to fetch details.

    Returns:
        dict: A dictionary containing detailed survey information
    """
    endpoint = f"https://api.surveymonkey.com/v3/surveys/{survey_id}/details"
    result = request_template(endpoint)
    return result

def get_survey_category():
    endpoint = f"https://api.surveymonkey.com/v3/survey_categories"
    result =  request_template(endpoint)
    return result

def get_survey_templates():
    endpoint = f"https://api.surveymonkey.com/v3/survey_templates"
    result =  request_template(endpoint)
    return result

def get_survey_pages(survey_id):
    endpoint = f"https://api.surveymonkey.com/v3/surveys/{survey_id}/pages"
    result = request_template(endpoint)
    return result

def get_survey_page_details(survey_id, page_id):
    endpoint = f"https://api.surveymonkey.com/v3/surveys/{survey_id}/pages/{page_id}"
    result = request_template(endpoint)
    return result

def get_survey_page_questions(survey_id, page_id):
    endpoint = f"https://api.surveymonkey.com/v3/surveys/{survey_id}/pages/{page_id}/questions"
    result = request_template(endpoint)
    return result


## ----------------------------------- Call the functions pulling data --------------------------------------------------------------------------------------------------------
#get_surveys()
# get_survey_details(417488166)
get_survey_page_questions(417488166, 63655056)