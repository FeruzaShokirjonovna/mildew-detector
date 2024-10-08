# Code adapted from Code Institute's Malaria walkthrough project

import base64
from datetime import datetime
import joblib

def download_dataframe_as_csv(df):
    """ Function to download a dataframe as csv file, we will use it to allow the users
        download the report """
    datetime_now = datetime.now().strftime("%d%b%Y_%Hh%Mmin%Ss")
    csv = df.to_csv().encode()
    b64 = base64.b64encode(csv).decode()
    href = (
        f'<a href="data:file/csv;base64,{b64}" download="Report {datetime_now}.csv" '  # noqa
        f'target="_blank">Download Report</a>'
    )
    return href



def load_pkl_file(file_path):
    """ Function to load a pkl file according to the file path variable """
    return joblib.load(filename=file_path)