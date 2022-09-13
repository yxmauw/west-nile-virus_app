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

mapboxt = open('./.gitignore/.mapbox_token.txt').read().rstrip()

fig = make_subplots(
    rows=1, cols=2,
    subplot_titles=("Plot 1", "Plot 2"),
    specs=[[{"type": "mapbox"}, {"type": "mapbox"}]])
          

fig.add_trace(go.Densitymapbox(lat=no_spray_df['Latitude'], lon=no_spray_df['Longitude'], z=no_spray_df['WnvPresent'], 
                    radius = 4,), 
              row=1, col=1)

fig.add_trace(go.Densitymapbox(lat=spray_df['Latitude'], lon=spray_df['Longitude'], z=spray_df['WnvPresent'], 
                    radius = 4,), 
              row=1, col=2)

#update the common attributes:
fig.update_mapboxes(
        accesstoken=mapboxt,
        center=dict(
            lat=41.85,
            lon=-87.7
        ),
        zoom=8)
   
#update different styles:
fig.update_layout(mapbox_style="carto-positron", mapbox2_style="carto-positron", coloraxis=dict(autocolorscale=False))
#fig.update_coloraxes(showscale=False)

# fig.update(layout_coloraxis_showscale=False) # removes default color scale on the side

st.plotly_chart(fig, use_container_width=False) 

