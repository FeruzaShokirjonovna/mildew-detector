# Code adapted from Code Institute's Malaria walkthrough project
import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.summary_page import summary_page_body
from app_pages.leaves_visualizer_page import leaves_visualizer_page_body
from app_pages.mildew_detector_page import mildew_detector_body
from app_pages.project_hypothesis_page import project_hypothesis_page_body
from app_pages.ml_performance_page import ml_performance_body

# Create an instance of the app
app = MultiPage(app_name= "Powdery Mildew Detector")

app.add_page('Quick Project Summary', summary_page_body)
app.add_page('Leaves Visualizer', leaves_visualizer_page_body)
app.add_page('Powdery Mildew Detector', mildew_detector_body)
app.add_page('Project Hypothesis', project_hypothesis_page_body)
app.add_page('ML Performance Metrics', ml_performance_body)

page_bg_img = '''
<style>
[data-testid="stReportViewContainer"]{
background-image: url("https://res.cloudinary.com/dlznujk9q/image/upload/v1724199056/vecteezy_green-leaves-flying-in-the-air-against-a-white-background_48479275_z6asq2.jpg");
background-size: cover;
background-position: center;

}
[data-testid="stSidebar"] > div:first-child {
background-image: url("https://res.cloudinary.com/dlznujk9q/image/upload/v1724199785/vecteezy_green-leaves-flying-in-the-air-against-a-white-background_48479275_z6asq2_Square_wqelt1.jpg");
}
[data-testid="stReportViewContainer"]::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.4); /* Dark overlay */
    z-index: -1;
    }
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

app.run() # Run the app