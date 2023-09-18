import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd

st.set_page_config(layout="wide")

st.title("Morocco Earthquake-COG Mosaic-Split Map")

m = leafmap.Map()

pre = leafmap.maxar_tile_url('Morocco-Earthquake-Sept-2023', '104001006800CE00', dtype='json')
post = leafmap.maxar_tile_url('Morocco-Earthquake-Sept-2023', '10300500E4F91700', dtype='json')

m.split_map(
    left_layer =pre, right_layer=post, left_label='pre-event', right_label='post-event',
)
m.set_center(-7.965421, 31.2265, 17)
m.to_streamlit(height=600)
