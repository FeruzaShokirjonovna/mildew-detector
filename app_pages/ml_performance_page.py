# Code adapted from Code Institute's Malaria walkthrough project

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation


def ml_performance_body():
    """ Function to show the ML performance page """
    # We are currently using the version 1
    version = 'v1'

    st.write("### Train, Validation and Test Sets: Labels Frequencies")
    # Display the labels frecuncies
    labels_distribution = plt.imread(f"outputs/{version}/labels_distribution.png")
    st.image(labels_distribution, caption='Labels Distribution on Train, Validation and Test Sets')
    st.info(
        "The images provided were split into train, test and validation sets, "
        "where the train set contains 70% of all images, the test set "
        "contains 20% and the validation set contains 10%.\n"
        "The plot above visualizes the split and shows that both labels "
        "are distributed evenly across the sets."
    )
    st.write("---")

    st.write("### Model History")
    # Display the Model History
    col1, col2 = st.beta_columns(2)
    with col1: 
        model_acc = plt.imread(f"outputs/{version}/model_training_acc.png")
        st.image(model_acc, caption='Model Traninig Accuracy')
    with col2:
        model_loss = plt.imread(f"outputs/{version}/model_training_losses.png")
        st.image(model_loss, caption='Model Traninig Losses')
    st.info(
        "The plots above show the accuracy and losses plots for the model "
        "trained with the Softmax activation function. We can see that there "
        "are some spikes in the validation, but other than that the curves "
        "follow each other closely and show a good progression as expected."
    )
    st.write("---")

    st.write("### Generalised Performance on Test Set")
    # Display the performance on test set
    st.dataframe(pd.DataFrame(load_test_evaluation(version),
                 index=['Loss', 'Accuracy'],
                 columns=['Performance']))
    
    