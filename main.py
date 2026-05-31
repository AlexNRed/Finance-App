import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import json
import os

st.set_page_config(page_title="Finance App", page_icon=":money_with_wings:", layout="wide")

def load_transactions(file):
    pass

def main():
    st.title("Finance Dashboard")

    uploaded_file = st.file_uploader("Upload your transation CSV file", type=["csv"])

    if uploaded_file is not None:
        df = load_transactions(uploaded_file)

main()