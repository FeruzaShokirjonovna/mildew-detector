import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread
import itertools
import random


def leaves_visualizer_page_body():
    """ Function to display the leaves visualizer page """
    st.write("### Leaves Visualizer")
    # Write the business requirement 1
    st.success(
        f"* The client is interested in conducting a study to visually differentiate a cherry leaf"
        f" that is healthy from one that contains powdery mildew.")
    
    # We are currently use the first version of the app
    version = 'v1'
    # Show average and variability of images
    if st.checkbox("Differences between average and variability images"):
      
        avg_var_healty = plt.imread(f"outputs/{version}/avg_var_healthy.png")
        avg_var_powdery_mildew = plt.imread(f"outputs/{version}/avg_var_powdery_mildew.png")

        st.success(
        f"* We notice the average images show that the infected leaves have a "
        f"color more white than the "
        f"healthy ones. Maybe they are qualities hard to appreciate when we are"
        f" looking only to one leaf"
        f", without the posibility of compare with other one of different kind."
        f" The variability images show more lines in the surface of the powdery"
        f" mildew infected leaves"
        f" than in the surface of the healthy ones, which are almost in plane "
        f"color. In this case it looks "
        f"not that hard to appreciate it when we are looking to only one leaf."
        )

        st.image(avg_var_healty, caption='Healty leaves - Avegare and Variability')
        st.image(avg_var_powdery_mildew, caption='Powdery Mildew infected leaves - Average and Variability')
        st.write("---")
    
    # Show the difference between average and variability images
    if st.checkbox("Differences between average healthy and average infected leaves"):
        diff_between_avgs = plt.imread(f"outputs/{version}/avg_diff.png")

        st.success(
        f"* We can appreciate the same pattern here, where the healthy leaves have a "
        f"surface more clear, green, and the infected ones have more white color in "
        f"the surface. Difficult to appreciate when we cannot compare both different"
        f" kind of leaves."
        )

        st.image(diff_between_avgs, caption='Difference between average images')
    # Show the image montage
    if st.checkbox("Image Montage"): 
        st.success(
            f"* The montage helps to visualize the difference between a healthy"
            f" leaf and an infected one. The infected one has white, powdery "
            f"spots or patches on the top side of leaves"
        )
        st.info("To refresh the montage, click on 'Create Montage' button")
        my_data_dir = 'inputs/cherry_dataset/cherry-leaves'
        labels = os.listdir(my_data_dir+ '/validation')
        label_to_display = st.selectbox(label="Select label", options=labels, index=0)
        if st.button("Create Montage"):      
            image_montage(dir_path= my_data_dir + '/validation',
                        label_to_display=label_to_display,
                        nrows=8, ncols=3, figsize=(10,25))
        st.write("---")
