import streamlit as st
from datetime import datetime
from api_client import create_patient, get_all_patients

def add_patient_form():
    """Display a form to add a new patient."""
    with st.form("patient_form", clear_on_submit=True):
        st.write("## Add New Patient")
        first_name = st.text_input("First Name").strip()
        last_name = st.text_input("Last Name").strip()
        date_of_birth = st.date_input("Date of Birth")
        email = st.text_input("Email").strip()
        phone_number = st.text_input("Phone Number").strip()
        address = st.text_input("Address").strip()
        submitted = st.form_submit_button("Submit")
        if submitted and first_name and last_name:
            patient_data = {
                "firstName": first_name,
                "lastName": last_name,
                "dateOfBirth": datetime.strftime(date_of_birth, '%Y-%m-%d'),
                "email": email,
                "phoneNumber": phone_number,
                "address": address
            }
            response_data, status_code = create_patient(patient_data)
            if status_code == 201:
                st.success("Patient added successfully")
            else:
                st.error("Failed to add patient")

def view_patients():
    """Display a list of existing patients."""
    st.write("## Patient Records")
    response_data, status_code = get_all_patients()
    if status_code == 200:
        for patient in response_data:
            st.write(f"ID: {patient['id']}, Name: {patient['firstName']} {patient['lastName']}, DOB: {patient['dateOfBirth']}")
    elif status_code == 404:
        st.error("No patients found")
    else:
        st.error("Failed to retrieve patients")

# Display the form and patient records
st.title("EMR System")
add_patient_form()
view_patients()
