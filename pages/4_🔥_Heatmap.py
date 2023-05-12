import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.title("Heatmap")

#filepath = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv"
#m = leafmap.Map(center=[40, -100], zoom=4, tiles="stamentoner")
filepath = "./data/modis.csv"
m = leafmap.Map(ccenter=[0, 0], zoom=2, tiles="stamentoner")

m.add_heatmap(
    filepath,
    #latitude="latitude",
    #longitude="longitude",
    #value="pop_max",
    latitude="LATITUDE",
    longitude="LONGITUDE",
    value="CONFIDENCE",
    name="Heat map",
    radius=15,
)
m.to_streamlit(height=700)
