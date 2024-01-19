import requests

# Define the base URL of the Express server
BASE_URL = 'http://localhost:3000/api/patients' # INPUT_REQUIRED {Enter the correct API URL, if different from localhost:3000}

def create_patient(patient_data):
    """Send a POST request to add a new patient."""
    response = requests.post(f"{BASE_URL}/", json=patient_data)
    return response.json(), response.status_code

def get_all_patients():
    """Send a GET request to retrieve all patients."""
    response = requests.get(BASE_URL)
    return response.json(), response.status_code
