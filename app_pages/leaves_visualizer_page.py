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