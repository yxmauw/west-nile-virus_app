import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import pickle
import plotly.figure_factory as ff

# https://plotly.com/python/mapbox-density-heatmaps/
@st.cache
def data(): 
    with open('st_no_sprayed.pkl', 'rb') as f:
        df = pickle.load(f)
    return df

df = data()

st.sidebar.title('🦟 Identifying presence of West Nile Virus per Trap')
st.sidebar.info('## What if all trap areas were not sprayed?')

px.set_mapbox_access_token(open('./.gitignore/.mapbox_token.txt').read())
# this format allows animation

fig = px.density_mapbox(df, 
                        lat='Latitude', 
                        lon='Longitude', 
                        z='WnvPresent', 
                        animation_frame=df.index,
                        radius=10,
                        center=dict(lat=0, lon=180), 
                        zoom=9,
                        height=650,
                        title='''Density map of West Nile Virus if all trap areas \n
                                 were NOT sprayed'''
                        )
fig.update_layout(mapbox_style="carto-positron", 
                  mapbox_center = {"lat": 41.85, "lon": -87.63})

# fig.update(layout_coloraxis_showscale=False) # removes default color scale on the side
st.plotly_chart(fig, use_container_width=True)
