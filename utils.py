import re
import requests


def clean_text(text: str) -> str:
    """
    Cleans the input text by removing HTML tags, URLs, non-alphanumeric characters, 
    and excess whitespace.

    Args:
        text (str): The text to be cleaned.

    Returns:
        str: The cleaned text.

    Notes:
        This function uses regular expressions to perform the following operations:
            - Remove HTML tags
            - Remove URLs (both HTTP and HTTPS)
            - Remove non-alphanumeric characters (except for spaces)
            - Replace multiple whitespace characters with a single space
            - Remove leading and trailing whitespace
    """
    text = re.sub(r'<[^>]*?>', '', text)
    text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)
    text = re.sub(r'\s{2,}', ' ', text)
    text = text.strip()
    text = ' '.join(text.split())
    return text


def get_model_list() -> list:
    """
    Retrieves a list of available model IDs from the Groq API.

    This function sends a GET request to the Groq API with a provided API key and 
    returns a list of model IDs.

    Returns:
        list: A list of model IDs available on the Groq API.

    Raises:
        requests.exceptions.RequestException: If the request to the Groq API fails.
    """
    api_key = ""
    url = "https://api.groq.com/openai/v1/models"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    model_list: list = []
    for model in response.json()['data']:
        model_list.append(model['id'])
    return model_list
