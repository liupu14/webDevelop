import streamlit as st 
from streamlit_folium import folium_static
import folium
import pandas as pd 

st.set_page_config(layout="wide")
"# streamlit-folium"

file = st.file_uploader("Pick a file")
if file:
    data = pd.read_excel(file)
    st.table(data.head())

m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)

# add marker for Liberty Bell
tooltip = "Liberty Bell"
folium.Marker(
    [39.949610, -75.150282], popup="Liberty Bell", tooltip=tooltip
).add_to(m)

# call to render Folium map in Streamlit
folium_static(m,width=1200,height=500)