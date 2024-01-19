import streamlit as st
from forms import add_patient_form
from view_patients import view_patients

# Display the form and patient records
st.title("EMR System")
add_patient_form()
view_patients()
