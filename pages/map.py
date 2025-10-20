import streamlit as st
import plotly.express as px
from utils.data_loader import load_data

def show():
    st.title("🗺️ Crime Map of Mexico City")
    st.markdown("Explore spatial patterns of crime incidents using geolocation data.")

    df = load_data()
    if df.empty:
        st.stop()

    if "latitud" not in df.columns or "longitud" not in df.columns:
        st.warning("No geographic data available.")
        st.stop()

    fig = px.scatter_mapbox(
        df,
        lat="latitud",
        lon="longitud",
        hover_name="delito",
        hover_data=["alcaldia_hecho", "fecha_hecho"],
        color_discrete_sequence=["red"],
        zoom=10,
        height=600,
    )

    fig.update_layout(mapbox_style="open-street-map", margin={"r":0,"t":0,"l":0,"b":0})
    st.plotly_chart(fig, use_container_width=True)
