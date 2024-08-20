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
        f"* Download a set of haelthy and powdery mildew infected leaves for live "
        f"prediction [here](https://www.kaggle.com/codeinstitute/cherry-leaves)"
        )

    st.write("---")
    # The file uploader is shown with three extensions allowed, png, jpg and jpeg.
    images_buffer = st.file_uploader('Upload leaves images samples. You may select more than one.',
                                        type=['png','jpg','jpeg'],accept_multiple_files=True)
