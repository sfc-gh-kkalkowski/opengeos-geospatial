import streamlit as st
import pandas as pd
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

url = 'https://raw.githubusercontent.com/opengeos/maxar-open-data/master'
repo = 'https://github.com/opengeos/maxar-open-data/blob/master/datasets'

m = leafmap.Map()

def get_datasets():
    datasets = f'{url}/datasets.csv'
    df = pd.read_csv(datasets)
    return df
def get_catalogs(name):
    dataset = f'{url}/datasets/{name}.tsv'
    dataset_df = pd.read_csv(dataset, sep='\t')
    catalog_ids = dataset_df['catalog_id'].unique().tolist()
    return catalog_ids

default = 'Kahramanmaras-turkey-earthquake-23'
datasets = get_datasets()['dataset'].tolist()
dataset = st.selectbox('Select a dataset', datasets, index=datasets.index(default))
catalog = st.selectbox('Select a COG mosaic', get_catalogs(dataset))

dataset
catalog

mosaic = f'https://open.gishub.org/maxar-open-data/datasets/{dataset}'
mosaic
m.to_streamlit(height=700)
