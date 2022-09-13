import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import pickle

# https://plotly.com/python/mapbox-density-heatmaps/
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

st.sidebar.title('🦟 Identifying presence of West Nile Virus per Trap')
st.sidebar.info('## What if all trap areas were not sprayed?')

#px.set_mapbox_access_token(open('./.gitignore/.mapbox_token.txt').read())
col1, col2 = st.columns(2) # format 2 columns 

with col1:
    fig = px.density_mapbox(no_spray_df, 
                            lat='Latitude', 
                            lon='Longitude', 
                            z='WnvPresent', 
                            animation_frame='Date',
                            zoom=9,
                            height=750,
                            title='Density map of West Nile Virus if all trap area were NOT sprayed'
                            )
    fig.update_layout(mapbox_style="carto-positron", 
                      mapbox_center = {"lat": 41.85, "lon": -87.63}
                      )

    fig.update(layout_coloraxis_showscale=False) # removes default color scale on the side
           
    st.plotly_chart(fig, use_container_width=True)
   
with col2:
     fig = px.density_mapbox(spray_df, 
                            lat='Latitude', 
                            lon='Longitude', 
                            z='WnvPresent', 
                            animation_frame='Date',
                            zoom=9,
                            height=750,
                            title='Density map of West Nile Virus if all trap area were ALL sprayed'
                            )
    fig.update_layout(mapbox_style="carto-positron", 
                      mapbox_center = {"lat": 41.85, "lon": -87.63}
                      )

    fig.update(layout_coloraxis_showscale=False) # removes default color scale on the side
           
    st.plotly_chart(fig, use_container_width=True) 
