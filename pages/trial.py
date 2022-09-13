import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pickle

st.set_page_config(layout="wide")

@st.cache
def data_no_spray(): 
    with open('st_no_sprayed.pkl', 'rb') as f:
        df = pickle.load(f)
    return df
def data_spray():
    with open('st_sprayed.pkl', 'rb') as f:
        df = pickle.load(f)
    return df

no_spray_df = data_no_spray().drop_duplicates()
spray_df = data_spray().drop_duplicates()

fig = make_subplots(
    rows=1, cols=2,
    subplot_titles=("Plot 1", "Plot 2"))

fig.add_trace(go.Densitymapbox(lat=no_spray_df['Latitude'], lon=no_spray_df['Longitude']), z=no_spray_df['WnvPresent'], 
                    radius = 4,
                    subplot=mapbox,
              row=1, col=1)

fig.add_trace(go.Densitymapbox(lat=spray_df['Latitude'], lon=['Longitude']), z=spray_df['WnvPresent'], 
                    radius = 4,
                    subplot=mapbox,
              row=1, col=2)

fig.update_layout(mapbox_style="carto-positron",  mapbox_center = {"lat": 41.85, "lon": -87.7})

fig.update(layout_coloraxis_showscale=False) # removes default color scale on the side

st.plotly_chart(fig, use_container_width=False) 