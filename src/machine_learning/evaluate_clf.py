import streamlit as st
from src.data_management import load_pkl_file

def load_test_evaluation(version):
    """ Function to load the evaluation file """
    return load_pkl_file(f'outputs/{version}/trainings/evaluation.pkl')