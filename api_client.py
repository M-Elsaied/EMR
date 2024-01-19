import requests
import os

BASE_URL = 'http://localhost:3000/api/patients'
BASE_AUTH_URL = 'http://localhost:3000/api/auth'

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'password'


def authenticate_user(username, password):
    """Authenticate user and retrieve JWT token."""
    response = requests.post(
        f"{BASE_AUTH_URL}/login",
        json={"username": username, "password": password}
    )
    if response.status_code == 200:
        token = response.json().get('token')
        return token
    else:
        return None

def get_headers():
    JWT_TOKEN = authenticate_user(ADMIN_USERNAME, ADMIN_PASSWORD)
    if JWT_TOKEN is not None:
        return {'Authorization': f'Bearer {JWT_TOKEN}'}
    else:
        raise Exception("Authentication failed")

def create_patient(patient_data):
    """Send a POST request to add a new patient."""
    headers = get_headers()
    response = requests.post(f"{BASE_URL}/", json=patient_data, headers=headers)
    return response.json(), response.status_code

def get_all_patients():
    """Send a GET request to retrieve all patients."""
    headers = get_headers()
    response = requests.get(BASE_URL, headers=headers)
    return response.json(), response.status_code
