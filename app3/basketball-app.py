import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import base64

st.title('NBA Player Stats Explorer')

st.markdown("""
This app performs simple webscraping of NBA player stats data!
* **Python libraries:** base64, pandas, streamlit
""")

st.siderbar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year', list(reversed(range(1950, 2021))))
