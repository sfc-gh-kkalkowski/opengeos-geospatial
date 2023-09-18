import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd

st.set_page_config(layout="wide")

st.title("Turkey Earthquake-COG Mosaic")

m = leafmap.Map()

#pre = leafmap.maxar_tile_url('Kahramanmaras-turkey-earthquake-23', '10300100D797E100', dtype='json')
pre = 'https://maxar-opendata.s3.amazonaws.com/events/Kahramanmaras-turkey-earthquake-23/ard/acquisition_collections/10300100D797E100_collection.json'

post = leafmap.maxar_tile_url('Kahramanmaras-turkey-earthquake-23', '10300500D9F8D200', dtype='json')

url = 'https://open.gishub.org/maxar-open-data/datasets/Kahramanmaras-turkey-earthquake-23/10300100D797E100.json'
m.add_stac_layer(url, name="Mosaic")

m.split_map(
    left_layer =pre, right_layer=post, left_label='pre-event', right_label='post-event',
)
 
m.set_center(36.9265, 37.5762, 16)

m.to_streamlit(height=700)
