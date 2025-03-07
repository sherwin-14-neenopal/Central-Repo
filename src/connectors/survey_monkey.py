import os
import httpx
import pandas as pd

from dotenv import load_dotenv
from typing import Optional

## Loading access token from config dir
load_dotenv("./config/.env")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")

def request_template(endpoint: int) -> Optional[dict]:
    """Send a request to SurveyMonkey API.

    This function is a general template that contains token for authorization along with the 
    logic for calling different API endpoints.This template is referenced in all the functions 
    below to handle the API request and response. The function returns the data if the 
    request is successful, or an error message if the request fails.

    Args:
        endpoint (int): The API endpoint to which the request is sent.

    Returns:
        None: The function returns the response data if the request is
        successful (status code 200), otherwise it prints an error message.
    """
    headers = {
        'Accept': "application/json",
        'Authorization': f"Bearer {ACCESS_TOKEN}"
    }
    response = httpx.get(endpoint, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")

def get_user() -> Optional[dict]:
    """Send a request to retrieve the user information.

    This function constructs a request to retrieve the details of the authenticated user.

    Returns:
        A dict containing the user data.
    """
    endpoint = f"https://api.surveymonkey.com/v3/users/me"
    result = request_template(endpoint)
    return result

def get_groups() -> Optional[dict]:
    """Send a request to retrieve a list of groups.

    This function constructs a request to retrieve all groups available in the SurveyMonkey account. 

    Returns:
        A dict containing the group data.
    """
    endpoint = f"https://api.surveymonkey.com/v3/groups"
    result = request_template(endpoint)
    return result


def get_surveys() -> Optional[dict]:
    """Send a request to retrieve a list of surveys.

    This function constructs a request to retrieve all surveys available in the SurveyMonkey account. 

    Returns:
        A dict containing the survey data.
    """
    endpoint = f"https://api.surveymonkey.com/v3/surveys"
    result = request_template(endpoint)
    return result


def get_survey_info(survey_id: int) -> Optional[dict]:
     """Send a request to retrieve information about a specific survey.

    This function constructs a request to retrieve detailed information about a survey identified by 
    the given survey ID from your SurveyMonkey account.

    Args:
        survey_id (int): The ID of the survey for which information is requested.

    Returns:
         A dict containing the survey information.
    """
     endpoint = f"https://api.surveymonkey.com/v3/surveys/{survey_id}"
     result = request_template(endpoint)
     return result

def get_survey_details(survey_id: int) -> Optional[dict]:
    """Fetch detailed information about a specific survey.

    This function constructs a request to retrieve detailed information about a survey, including its 
    pages and questions from your SurveyMonkey account.

    Args:
        survey_id (int): The ID of the survey for which to fetch details.

    Returns:
        A dict containing detailed survey information.
    """
    endpoint = f"https://api.surveymonkey.com/v3/surveys/{survey_id}/details"
    result = request_template(endpoint)
    return result

def get_survey_category() -> Optional[dict]:
    """Send a request to retrieve a list of survey categories.

    This function constructs a request retrieve all available survey categories from SurveyMonkey.

    Returns:
       A dict containing the survey categories.
    """
    endpoint = f"https://api.surveymonkey.com/v3/survey_categories"
    result =  request_template(endpoint)
    return result

def get_survey_templates() -> Optional[dict]:
    """Send a request to retrieve a list of survey templates.

    This function constructs a request retrieve all available survey templates in the SurveyMonkey.

    Returns:
        A dict containing the survey templates.
    """
    endpoint = f"https://api.surveymonkey.com/v3/survey_templates"
    result =  request_template(endpoint)
    return result

def get_survey_pages(survey_id: int) -> Optional[dict]:
    """Send a request to retrieve the pages of a specific survey.

    This function constructs a request to retrieve all pages associated with the survey identified 
    by the given survey ID.

    Args:
        survey_id (int): The ID of the survey for which pages are requested.

    Returns:
        A dict containing all the pages of a survey.
    """
    endpoint = f"https://api.surveymonkey.com/v3/surveys/{survey_id}/pages"
    result = request_template(endpoint)
    return result

def get_survey_page_details(survey_id: int, page_id: int) -> Optional[dict]:
    """Send a request to retrieve details of a specific survey page.

    This function constructs a request to retrieve detailed information about a page 
    associated with the survey identified by the given survey ID and page ID. 

    Args:
        survey_id (int): The ID of the survey to which the page belongs.
        page_id (int): The ID of the page for which details are requested.

    Returns:
        A dict containing detailed infomation of a page.
    """
    endpoint = f"https://api.surveymonkey.com/v3/surveys/{survey_id}/pages/{page_id}"
    result = request_template(endpoint)
    return result

def get_survey_page_questions(survey_id: int, page_id: int) -> Optional[dict]:
    """Send a request to retrieve questions from a specific survey page.

    This function constructs a request to retrieve all questions associated with the page 
    identified by the given survey ID and page ID. 

    Args:
        survey_id (int): The ID of the survey to which the page belongs.
        page_id (int): The ID of the page for which questions are requested.
        
    Returns:
        A dict containing all questions from the specified page.
    """
    endpoint = f"https://api.surveymonkey.com/v3/surveys/{survey_id}/pages/{page_id}/questions"
    result = request_template(endpoint)
    return result

def get_survey_question_details(survey_id: int, page_id: int, question_id: int):
    """Send a request to retrieve details of a specific survey question.

    This function constructs a request to retrieve detailed information about a 
    question associated with the page identified by the given survey ID, page ID, 
    and question ID.

    Args:
        survey_id (int): The ID of the survey to which the question belongs.
        page_id (int): The ID of the page that contains the question.
        question_id (int): The ID of the question for which details are requested.

    Returns:
        A dict containing the details of the specified question or None.
    """
    endpoint = f"https://api.surveymonkey.com/v3/surveys/{survey_id}/pages/{page_id}/questions/{question_id}"
    result = request_template(endpoint)
    return result

def get_survey_folders() -> Optional[dict]:
    """Send a request to retrieve a list of survey folders.

    This function constructs a request retrieve all available survey folders from SurveyMonkey.

    Returns:
        A dict containing the survey folders.
    """
    endpoint = f"https://api.surveymonkey.com/v3/survey_folders"
    result = request_template(endpoint)
    return result

def get_survey_responses(survey_id: int) -> Optional[dict]:
    """Send a request to retrieve responses for a specific survey.

    This function constructs a request to retrieve all responses associated with the 
    survey identified by the given survey ID.

    Args:
        survey_id (int): The ID of the survey for which responses are requested.

    Returns:
        A dict containing the survey responses for a survey.
    """
    endpoint = f"https://api.surveymonkey.com/v3/surveys/{survey_id}/responses"
    result = request_template(endpoint)
    return result

def get_survey_response_by_id(survey_id: int, response_id: int) -> Optional[dict]:
    """Send a  request to retrieve a specific response for a survey.

    This function constructs a request to retrieve a single response associated with the 
    survey identified by the given survey ID and response ID. 

    Args:
        survey_id (int): The ID of the survey for which the response is requested.
        response_id (int): The ID of the specific response to retrieve.

    Returns:
        A dict containing the specific survey response for a survey.
    """
    endpoint = f"https://api.surveymonkey.com/v3/surveys/{survey_id}/responses/{response_id}"
    result  = request_template(endpoint)
    return result

def get_survey_response_details_by_id(survey_id: int, response_id: int) -> Optional[dict]:
    """Send a request to retrieve detailed information for a specific survey response.

    This function constructs a request to retrieve detailed information associated with a 
    specific response identified by the given survey ID and response ID. 

    Args:
        survey_id (int): The ID of the survey for which the response details are requested.
        response_id (int): The ID of the specific response for which details are to be .

    Returns:
        A dict containing the detailed information of the specific survey response.
    """
    endpoint = f"https://api.surveymonkey.com/v3/surveys/{survey_id}/responses/{response_id}/details"
    result = request_template(endpoint)
    return result

def get_survey_responses_bulk(survey_id: int) -> Optional[dict]:
    """Send a request to retrieve bulk responses for a specific survey.

    This function constructs a request to retrieve all responses associated with the survey 
    identified by the given survey ID in bulk. 

    Args:
        survey_id (int): The ID of the survey for which bulk responses are requested.

    Returns:
        A dict containing the bulk responses for the specified survey.
    """
    endpoint = f"https://api.surveymonkey.com/v3/surveys/{survey_id}/responses/bulk"
    result = request_template(endpoint)
    return result

def get_survey_rollups(survey_id: int) -> Optional[dict]:
    """Send a request to retrieve rollup data for a specific survey.

    This function constructs a request to retrieve rollup data associated with the survey 
    identified by the given survey ID. 

    Args:
        survey_id (int): The ID of the survey for which rollup data is requested.

    Returns:
        A dict containing the rollup data for the specified survey.
    """
    endpoint = f"https://api.surveymonkey.com/v3/surveys/{survey_id}/rollups"
    result = request_template(endpoint)
    return result

def get_survey_question_rollups(survey_id: int, page_id: int, question_id: int) -> Optional[dict]:
    """Send a request to retrieve rollup data for a specific question in a survey.

    This function constructs a request to retrieve rollup data associated with a specific 
    question identified by the given survey ID, page ID, and question ID. 

    Args:
        survey_id (int): The ID of the survey containing the question.
        page_id (int): The ID of the page containing the question.
        question_id (int): The ID of the specific question for which rollup data is requested.

    Returns:
        A dict containing the rollup data for the specified question in the survey.

    """
    endpoint = f"https://api.surveymonkey.com/v3/surveys/{survey_id}/pages/{page_id}/questions/{question_id}/rollups"
    result = request_template(endpoint)
    return result

def get_survey_trends(survey_id: int) -> Optional[dict]:
    """Send a request to retrieve trend data for a specific survey.

    This function constructs a request retrieve trend data associated with the survey identified 
    by
    the given survey ID. 

    Args:
        survey_id (int): The ID of the survey for which trend data is requested.

    Returns:
        A dict containing the trend data for the specified survey.
    """
    endpoint = f"https://api.surveymonkey.com/v3/surveys/{survey_id}/trends"
    result = request_template(endpoint)
    return result

def get_survey_question_trends(survey_id: int, page_id: int, question_id: int) -> Optional[dict]:
    """Send a request to retrieve trend data for a specific question in a survey.

    This function constructs a request to retrieve trend data associated with a specific 
    question identified by the given survey ID, page ID, and question ID. 

    Args:
        survey_id (int): The ID of the survey containing the question.
        page_id (int): The ID of the page containing the question.
        question_id (int): The ID of the specific question for which trend data is requested.

    Returns:
        A dict containing the trend data for the specified question in the survey.
    """
    endpoint = f"https://api.surveymonkey.com/v3/surveys/{survey_id}/pages/{page_id}/questions/{question_id}/trends"
    result = request_template(endpoint)
    return result

def get_collectors(survey_id: int) -> Optional[dict]:
    """Send a request to retrieve collectors for a specific survey.

    This function constructs a request to retrieve all collectors associated with the survey 
    identified by the given survey ID. 

    Args:
        survey_id (int): The ID of the survey for which collectors are requested.

    Returns:
        A dict containing the collectors for the specified survey.
    """
    endpoint = f"https://api.surveymonkey.com/v3/surveys/{survey_id}/collectors"
    result  = request_template(endpoint)
    return result

def get_collector_responses(collector_id: int) -> Optional[dict]:
    """Send a request to retrieve responses for a specific collector.

    This function constructs a request retrieve all responses associated with the collector 
    identified by the given collector ID.

    Args:
        collector_id (int): The ID of the collector for which responses are requested.

    Returns:
        A dict containing the responses for the specified collector.
    """
    endpoint = f"https://api.surveymonkey.com/v3/collectors/{collector_id}/responses"
    result = request_template(endpoint)
    return result

def get_collector_response_by_id(collector_id: int, response_id: int) -> Optional[dict]:
    """Send a request to retrieve a specific response for a collector.

    This function constructs a request to retrieve a response associated with the collector 
    identified by the given collector ID and response ID. 

    Args:
        collector_id (int): The ID of the collector for which the response is requested.
        response_id (int): The ID of the specific response to retrieve.

    Returns:
        A dict containing the specific response for the specified collector.
    """
    endpoint = f"https://api.surveymonkey.com/v3/collectors/{collector_id}/responses/{response_id}"
    result = request_template(endpoint)
    return result

def get_collector_responses_bulk(collector_id: int) -> Optional[dict]:
    """Send a request to retrieve bulk responses for a specific collector.

    This function constructs a request to retrieve all responses associated with the collector 
    identified by the given collector ID in bulk. 

    Args:
        collector_id (int): The ID of the collector for which bulk responses are requested.

    Returns:
        A dict containing the bulk responses for the specified collector.
    """
    endpoint = f"https://api.surveymonkey.com/v3/collectors/{collector_id}/responses/bulk"
    result = request_template(endpoint)
    return result

def get_contacts() -> Optional[dict]:
    """Send a request to retrieve all contacts.

    This function constructs a request to retrieve a list of all contacts associated with the 
    account. 

    Returns:
        A dict containing the list of contacts associated with the account.
    """
    endpoint = f"https://api.surveymonkey.com/v3/contacts"
    result = request_template(endpoint)
    return result

def get_survey_languages(survey_id: int) -> Optional[dict]:
    """Send a request to retrieve the languages available for a specific survey.

    This function constructs a request to retrieve a list of languages associated with the survey 
    identified by the given survey ID. 

    Args:
        survey_id (int): The ID of the survey for which languages are requested.

    Returns:
        A dict containing the languages available for the specified survey.
    """
    endpoint = f"https://api.surveymonkey.com/v3/surveys/{survey_id}/languages"
    result = request_template(endpoint)
    return result


## ----------------------------------- Call the functions pulling data --------------------------------------------------------------------------------------------------------
## Survey id - 417488166
## Collector id  - 435022908
## Response id - 114810765595
## Page id - 63655056
## Question id - 235189687
print(get_contacts())