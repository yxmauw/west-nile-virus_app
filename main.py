import streamlit as st
import pandas as pd
import numpy as np
import time 
import plotly.express as px

# https://plotly.github.io/plotly.py-docs/generated/plotly.express.scatter_mapbox.html
# https://plotly.com/python/scattermapbox/
@st.cache
def data(): 
    df = pd.read_csv('./train.csv')
    return df

# traps.rename(columns={'Longitude':'longitude',
                      #'Latitude':'latitude'}, inplace=True) # st.map only recognised these col names

df = data()
trap_locations = df[['Longitude', 'Latitude','Trap','Date']].drop_duplicates()

# map
st.sidebar.title('🦟 Identifying presence of West Nile Virus per Trap')
st.sidebar.info('## All Traps 🪤 map')
# st.map(locations) # plots all points at once
px.set_mapbox_access_token(open('.mapbox_token.txt').read())
# this format allows animation
fig = px.scatter_mapbox(trap_locations, 
                        lat="Latitude", 
                        lon="Longitude",     
                        color="Trap",
                        color_discrete_sequence=['blue'],
                        size_max=15, 
                        #animation_frame="Date",
                        zoom=9,
                        height=650,
                        title='Map showing Trap locations')
fig.update_layout(mapbox_style="carto-positron", 
                  #mapbox_zoom=10, 
                  mapbox_center = {"lat": 41.85, "lon": -87.63})

fig.update(layout_coloraxis_showscale=False) # removes default color scale on the side
st.plotly_chart(fig, use_container_width=True)

#for i in range(len(locations)):
    #background.add_rows(locations)
    # Sleep for a moment just for demonstration purposes, so that the new data
    # animates in.
    #time.sleep(0.1)
