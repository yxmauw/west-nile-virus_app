import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import pickle
import plotly.graph_objects as go
import time
import matplotlib.pyplot as plt

# https://plotly.com/python/mapbox-density-heatmaps/
@st.cache
def data(): 
    with open('st_no_sprayed.pkl', 'rb') as f:
        df = pickle.load(f)
    return df

df = data()
#df1 = df.head(10)
#df2 = df.iloc[10:]

st.sidebar.title('🦟 Identifying presence of West Nile Virus per Trap')
st.sidebar.info('## What if all trap areas were not sprayed?')

#px.set_mapbox_access_token(open('./.gitignore/.mapbox_token.txt').read())

mapdata = np.loadtxt("mapdata_copyright_openstreetmap_contributors.txt")
# set up base map
aspect = mapdata.shape[0] * 1.0 / mapdata.shape[1]
lon_lat_box = (-88.0, -87.5, 41.6, 42.1)

fig = plt.imshow(mapdata, 
           cmap=plt.get_cmap('gray'), 
           extent=lon_lat_box, 
           aspect=aspect,
           figsize=(10,14) )
st.pyplot(fig)

#fig = px.scatter_mapbox(df1, 
                        #lat='Latitude', 
                        #lon='Longitude', 
                        #color='WnvPresent', 
                        #zoom=9,
                        #height=650,
                        #title='''Density map of West Nile Virus if all trap area were NOT sprayed'''
                        #)
#fig.update_layout(mapbox_style="carto-positron", 
                  #mapbox_center = {"lat": 41.85, "lon": -87.63},
                  #height=650,
                  #title='Density map of West Nile Virus if all trap area were NOT sprayed')

#fig.update(layout_coloraxis_showscale=False, 
           #) # removes default color scale on the side
#f = go.FigureWidget(fig)
#st.plotly_chart(f, use_container_width=True)
#chart = st.plotly_chart(fig, use_container_width=True)

#for i in range(len(df2)):
   # chart.add_rows(df2) 
    # Sleep for a moment just for demonstration purposes, so that the new data
    # animates in.
    #time.sleep(0.1)
