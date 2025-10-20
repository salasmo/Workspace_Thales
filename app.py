import streamlit as st
from pages import dashboard, map

# ===============================
# App configuration
# ===============================
st.set_page_config(
    page_title="CDMX Crime Analytics Dashboard",
    layout="wide",
    page_icon="📊"
)

# Sidebar navigation
st.sidebar.title("🔍 Navigation")
page = st.sidebar.radio("Go to:", ["Dashboard", "Crime Map"])

# Display selected page
if page == "Dashboard":
    dashboard.show()
elif page == "Crime Map":
    map.show()