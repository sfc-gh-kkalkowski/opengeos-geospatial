import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.title("Turkey Earthquake-Split Map")

url_pre = 'https://maxar-opendata.s3.us-west-2.amazonaws.com/events/Kahramanmaras-turkey-earthquake-23/ard/37/031131233233/2022-07-26/10300100D797E100-visual.tif'
url_post = 'https://maxar-opendata.s3.us-west-2.amazonaws.com/events/Kahramanmaras-turkey-earthquake-23/ard/37/031131233233/2023-02-08/10300500D9F8D200-visual.tif'

m = leafmap.Map()
m.split_map(
   left_layer = url_pre, right_layer= url_post, left_label='pre-event', right_label='post-event',
   )

m.set_center(36.9265, 37.5762, 16)
m.to_streamlit(height=600)
