# Code adapted from Code Institute's Malaria walkthrough project
import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.summary_page import summary_page_body
from app_pages.leaves_visualizer_page import leaves_visualizer_page_body
from app_pages.mildew_detertor_page import mildew_detector_body
from app_pages.project_hypothesis_page import project_hypothesis_page_body
from app_pages.ml_performance_page import ml_performance_body

# Create an instance of the app
app = MultiPage(app_name= "Powdery Mildew Detector")

app.add_page('Quick Project Summary', summary_page_body)
app.add_page('Leaves Visualizer', leaves_visualizer_page_body)
app.add_page('Powdery Mildew Detector', mildew_detector_body)
app.add_page('Project Hypothesis', project_hypothesis_page_body)
app.add_page('ML Performance Metrics', ml_performance_body)


app.run() # Run the app