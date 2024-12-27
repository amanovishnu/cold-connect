import requests


def get_model_list():
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