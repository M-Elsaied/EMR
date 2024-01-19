import streamlit as st
from api_client import get_all_patients

def view_patients():
    """Display a list of existing patients."""
    st.write("## Patient Records")
    try:
        response_data, status_code = get_all_patients()
        if status_code == 200 and response_data:
            for patient in response_data:
                st.write(f"ID: {patient['id']}, Name: {patient['firstName']} {patient['lastName']}, DOB: {patient['dateOfBirth']}")
        elif status_code == 200 and not response_data:
            st.info("No patients found")
    except Exception as e:
        st.error(f"An unexpected error occurred while fetching patient records: {e}")
