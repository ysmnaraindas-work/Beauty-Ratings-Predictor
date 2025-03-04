import streamlit as st

# Konfigurasi halaman harus berada paling atas
st.set_page_config(
    layout="wide",
    page_title="Sephora Skincare Product Rating Analysis",
    page_icon="https://cdn-icons-png.freepik.com/256/2553/2553642.png?semt=ais_hybrid",
)

# Import modul setelah konfigurasi halaman
import home
import eda
import predict

# Setup Tabs
tab1, tab2, tab3 = st.tabs(["Home", "Exploratory Data Analysis (EDA)", "Prediction"])

# Tab 1: Home
with tab1:
    home.run()

# Tab 2: Exploratory Data Analysis
with tab2:
    eda.run()

# Tab 3: Prediction
with tab3:
    predict.run()
