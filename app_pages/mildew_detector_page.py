import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analysis import (
                                                    load_model_and_predict,
                                                    resize_input_image,
                                                    plot_predictions_probabilities
                                                    )

# Treatment recommendations database
treatment_db = {
    "Powdery Mildew": {
        "description": "Powdery mildew is a fungal disease that affects many plants, including apple trees.",
        "treatments": [
            "Apply fungicides containing sulfur or potassium bicarbonate.",
            "Prune and destroy infected plant parts.",
            "Improve air circulation around plants.",
            "Avoid overhead watering to keep leaves dry."
        ],
        "resources": [
            "https://extension.umn.edu/plant-diseases/powdery-mildew-apple",
            "https://www2.ipm.ucanr.edu/agriculture/apple/Powdery-Mildew/"
        ]
    },
    "Healthy": {
        "description": "The leaf appears to be healthy with no visible signs of disease.",
        "treatments": [
            "Continue regular maintenance and care.",
            "Monitor for any signs of stress or disease.",
            "Maintain proper watering and fertilization schedules."
        ],
        "resources": [
            "https://extension.umn.edu/yard-and-garden/growing-apple-trees-home-garden",
            "https://www.rhs.org.uk/fruit/apples/grow-your-own"
        ]
    }
}

def get_treatment_suggestions(pred_class):
    """Fetch treatment suggestions based on prediction class."""
    return treatment_db.get(pred_class, {
        "description": "Unknown condition",
        "treatments": ["Consult a local plant pathologist or extension service for accurate diagnosis and treatment."],
        "resources": ["https://www.apsnet.org/Pages/default.aspx"]
    })

def display_treatment_suggestions(treatment_info):
    """Display treatment suggestions in a user-friendly format."""
    st.subheader("Treatment Suggestions")
    st.write(treatment_info["description"])
    st.write("Recommended treatments:")
    for treatment in treatment_info["treatments"]:
        st.write(f"- {treatment}")
    st.write("Additional resources:")
    for resource in treatment_info["resources"]:
        st.write(f"- [{resource}]({resource})")


def mildew_detector_body():
    """ Function to display the mildew detection page """
    # Business requirement 2
    st.success(
        f"The client is interested in predicting if a cherry leaf is healthy "
        f"or contains powdery mildew."
        )
    # The user must be able to donwload some images to test the application 
    # if the don't have any other image to do it, so the link
    # to the dataset is shown to them.
    st.write(
        f"* Download a set of healthy and powdery mildew infected leaves for live "
        f"prediction [here](https://www.kaggle.com/codeinstitute/cherry-leaves)"
        )

    st.write("---")
    # The file uploader is shown with three extensions allowed, png, jpg and jpeg.
    images_buffer = st.file_uploader('Upload a clear picture of a cherry leaf for live predictions. You may select more than one.',
                                        type=['png','jpg','jpeg'],accept_multiple_files=True)

    # if the user load at least one image, we can analyze the image in real time and show them 
    # the report and allow download it using the function imported from data_managment
    if images_buffer is not None:
        df_report = pd.DataFrame([])
        for image in images_buffer:

            img_pil = (Image.open(image))
            st.info(f"Leaf image Sample: **{image.name}**")
            img_array = np.array(img_pil)
            st.image(img_pil)

            version = 'v1'
            resized_img = resize_input_image(img=img_pil, version=version)
            pred_proba, pred_class = load_model_and_predict(resized_img, version=version)
            plot_predictions_probabilities(pred_proba, pred_class)

            treatment_info = get_treatment_suggestions(pred_class)
            display_treatment_suggestions(treatment_info)

            df_report = df_report.append({"Name":image.name, 'Result': pred_class },
                                        ignore_index=True)
        
            

        if not df_report.empty:
            st.success("Analysis Report")
            st.table(df_report)
            st.markdown(download_dataframe_as_csv(df_report), unsafe_allow_html=True)