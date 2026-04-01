import requests
from config.config import BASE_URL

def build_url(endpoint):
    return BASE_URL + endpoint

def get(endpoint):
    return requests.get(build_url(endpoint))

def post(endpoint, payload):
    return requests.post(build_url(endpoint), json=payload)

def put(endpoint, payload):
    return requests.put(build_url(endpoint), json=payload)

def delete(endpoint):
    return requests.delete(build_url(endpoint))

def login(username, password):
    response = requests.post(
        build_url("/auth/login"),
        json={
            "username": username,
            "password": password
        }
    )
    return response