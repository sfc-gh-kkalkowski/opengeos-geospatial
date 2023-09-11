
import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd

st.set_page_config(layout="wide")

st.title("Turkey Earthquake-Split Map")

m = leafmap.Map()


url_pre = 'https://maxar-opendata.s3.us-west-2.amazonaws.com/events/Kahramanmaras-turkey-earthquake-23/ard/37/031131233233/2023-02-08/10300500D9F8D200-visual.tif'

url_post = 'https://maxar-opendata.s3.us-west-2.amazonaws.com/events/Kahramanmaras-turkey-earthquake-23/ard/37/031131233233/2023-02-08/10300500D9F8D200-visual.tif'

m.split_map(
   left_layer = url_pre, right_layer= url_post, left_label='pre-event', right_label='post-event',
   )

m.set_center(36.9265, 37.5762, 16)
