import streamlit as st
import leafmap.foliumap as leafmap
import os

st.set_page_config(layout="wide")


st.title("California Fire-Split Map")

#os.environ['TITILER_ENDPOINT'] = 'https://titiler.xyz'

#Map = leafmap.Map()

url = 'https://opendata.digitalglobe.com/events/california-fire-2020/pre-event/2018-02-16/pine-gulch-fire20/1030010076004E00.tif'
#m.add_cog_layer(url, name="Fire (pre-event)")

url2 = 'https://opendata.digitalglobe.com/events/california-fire-2020/post-event/2020-08-14/pine-gulch-fire20/10300100AAC8DD00.tif'
#m.add_cog_layer(url2, name="Fire (post-event)")

#with st.expander("See source code"):
#with st.echo():
m = leafmap.Map(zoom=4)
m.split_map(
   left_layer = url, right_layer= url2, left_label='pre-event', right_label='post-event',
   )
#m.add_legend(title='ESA Land Cover', builtin_legend='ESA_WorldCover')

m.set_center(-108.564178,39.451119,14)

url3 = "https://unosat-datahub.cern.ch/geoserver/geonode/wms?"
m.add_wms_layer(
    url3, layers="MODIS_C6_1_Global_7d", format='image/png', transparent=True, name="Hot Spots"
)

m.to_streamlit(height=700)
