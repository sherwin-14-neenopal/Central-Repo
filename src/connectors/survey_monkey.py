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

def get_survey_question_details(survey_id, page_id, question_id):
    endpoint = f"https://api.surveymonkey.com/v3/surveys/{survey_id}/pages/{page_id}/questions/{question_id}"
    result = request_template(endpoint)
    return result

def get_survey_folders():
    endpoint = f"https://api.surveymonkey.com/v3/survey_folders"
    result = request_template(endpoint)
    return result

def get_survey_responses(survey_id):
    endpoint = f"https://api.surveymonkey.com/v3/surveys/{survey_id}/responses"
    result = request_template(endpoint)
    return result

def get_survey_response_by_id(survey_id, response_id):
    endpoint = f"https://api.surveymonkey.com/v3/surveys/{survey_id}/responses/{response_id}"
    result  = request_template(endpoint)
    return result

def get_survey_responses_bulk(survey_id):
    endpoint = f"https://api.surveymonkey.com/v3/surveys/{survey_id}/responses/bulk"
    result = request_template(endpoint)
    return result

def get_collectors(survey_id):
    endpoint = f"https://api.surveymonkey.com/v3/surveys/{survey_id}/collectors"
    result  = request_template(endpoint)
    return result

def get_collector_responses(collector_id):
    endpoint = f"https://api.surveymonkey.com/v3/collectors/{collector_id}/responses"
    result = request_template(endpoint)
    return result

def get_collector_responses_bulk(collector_id):
    endpoint = f"https://api.surveymonkey.com/v3/collectors/{collector_id}/responses/bulk"
    result = request_template(endpoint)
    return result



## ----------------------------------- Call the functions pulling data --------------------------------------------------------------------------------------------------------
## Survey id - 417488166
## Collector id  - 435022908
## Response id - 114810765595

get_survey_response_by_id(417488166, 114810765595)