import requests
import json
from configuration import *
from data import *
user_token = None


def create_new_user():
    url = BASE_URL + CREATE_USER_PATH
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=json.dumps(new_user_data))
    return response.json()["authToken"]


def get_new_user_token():
    global user_token
    if user_token is None:
        user_token = create_new_user()
    return user_token


def post_new_client_kit(kit_body, auth_token):
    url = BASE_URL + CREATE_KIT_PATH
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {auth_token}'
    }
    response = requests.post(url, headers=headers, data=json.dumps(kit_body))
    return response
