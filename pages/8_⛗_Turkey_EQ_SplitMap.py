
import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd

st.set_page_config(layout="wide")

st.title("Turkey Earthquake-Split Map")

m = leafmap.Map()


url_pre = 'https://maxar-opendata.s3.us-west-2.amazonaws.com/events/Morocco-Earthquake-Sept-2023/ard/29/120202012211/2021-05-02/104001006800CE00-visual.tif'

url_post = 'https://maxar-opendata.s3.us-west-2.amazonaws.com/events/Morocco-Earthquake-Sept-2023/ard/29/120202012211/2023-09-10/10300500E4F91700-visual.tif'

m.split_map(
   left_layer = url_pre, right_layer= url_post, left_label='pre-event', right_label='post-event',
   )

m.set_center(-7.98, 31.24, 16)
