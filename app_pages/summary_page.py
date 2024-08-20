import streamlit as st
import matplotlib.pyplot as plt

# Function to check if the warning message has been shown
def check_warning_message_state():
    '''
    Checks if the warning message has been shown.
    '''

    if 'warning_shown' not in st.session_state:
        st.session_state.warning_shown = False

# Function to show the warning message
def show_warning_message():
    
def summary_page_body():
    """ Funtion to show the summary page """
    st.write("### Quick Project Summary")
