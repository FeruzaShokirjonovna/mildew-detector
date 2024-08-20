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
    '''
    Displays the warning message recommending light mode over dark mode.
    '''

    if not st.session_state.warning_shown:
        placeholder = st.empty()
        placeholder.markdown('<div style="background-color: #FFEEEB; padding: 30px; margin-top: 40px; border-radius: 5px; text-align: center;"><p style="font-size: 20px; color: #333333"><strong>For better visualization, it is recommended to use Light mode instead of Dark mode in Settings.</strong></p></div>', unsafe_allow_html=True)
        st.session_state.warning_shown = True

        time.sleep(5)  # Wait for 5 seconds
        placeholder.empty()


def summary_page_body():
    """ Function to show the summary page """

    check_warning_message_state()
    show_warning_message()

    st.write("### Quick Project Summary"
    f"**General Information**\n"
    f"* The Project aims to assist farmers and agricultural professionals in identifying and managing plant diseases efficiently in apple trees.\n"
    f"* The system will focus on classifying apple plant images into two categories: Healthy and Powdery Mildew Affected.\n"
    f"* Powdery mildew is a fungal disease that affects a wide range of plants. Powdery mildew diseases are caused by many different species of fungi in the order Erysiphales."
    f"It is important to be aware of powdery mildew and its management as the resulting disease can significantly reduce important crop yields, [Powdery image](https://media.istockphoto.com/photos/grapevine-diseases-downy-mildew-is-a-fungal-disease-that-affects-a-picture-id1161364148?k=6&m=1161364148&s=612x612&w=0&h=BzE8nsZHyGD3y7r1wvKIYDrvqLQcJdk_efFCUNB3134=)\n"
    f"* Visual criteria are used to detect plant disease.\n"
    f"\n"
    f"**Project Dataset**\n"
    f"* The available dataset contains 4208 thousand images taken from "
    f"different leaves, half infected and half healthy."
    )

    # Link to the README file
    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/FeruzaShokirjonovna/mildew-detector/blob/main/README.md).")
    
    # Project business requirements
    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in conducting a study to "
        f"differentiate a cherry leaf"
        f" that is healthy from one that contains powdery mildew.\n"
        f"* 2 - The client is interested to predict if a cherry leaf is healthy"
        f" or contains powdery"
        f" mildew ")