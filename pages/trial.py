import streamlit as st
import numpy as np
import pandas as pd
#import plotly.graph_objects as go
#import plotly.express as px
#from plotly.subplots import make_subplots
import pickle
import matplotlib.pyplot as plt
import time

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
def mapdata():
    with open('mapdata.pkl', 'rb') as f:
        df = pickle.load(f)
    return df

no_spray_df = data_no_spray().drop_duplicates()
spray_df = data_spray().drop_duplicates()
mapdata = mapdata()

#mapboxt = open('./.gitignore/.mapbox_token.txt').read().rstrip()

# set up base map
aspect = mapdata.shape[0] * 1.0 / mapdata.shape[1]
lon_lat_box = (-88.0, -87.5, 41.6, 42.1)

# creating initial data values
# of x and y
x = (no_spray_df['Longitude'])[:10]
y = (no_spray_df['Latitude'])[:10]

# to run GUI event loop
plt.ion()

# here we are creating sub plots
fig, ax = plt.subplots(figsize=(10,14))
scatter = ax.scatter(x, y)

ax.imshow(mapdata, 
          cmap=plt.get_cmap('gray'), 
          extent=lon_lat_box, 
          aspect=aspect)

# setting x-axis label and y-axis label
plt.xlabel("Longitude")
plt.ylabel("Latitude")

# Loop
for i in range(len(no_spray_df):
    # creating new Y values
    new_y = (no_spray_df['Latitude'])[(i + 10) : (i + 20)]
    new_x = (no_spray_df['Longitude'])[(i + 10) : (i + 20)]
 
    # updating data values
    line1.set_xdata(new_x)
    line1.set_ydata(new_y)
 
    # drawing updated values
    figure.canvas.draw()
 
    # This will run the GUI event
    # loop until all UI events
    # currently waiting have been processed
    figure.canvas.flush_events()
 
    time.sleep(0.1)

st.pyplot(fig)
###########

#fig = make_subplots(
   # rows=1, cols=2,
   # subplot_titles=("Plot 1", "Plot 2"),
   # specs=[[{"type": "mapbox"}, {"type": "mapbox"}]])
          
#fig.add_trace(px.density_mapbox(no_spray_df, 
                            #lat='Latitude', 
                           # lon='Longitude', 
                           # z='WnvPresent', 
                           # animation_frame='Date',
                          #  zoom=9,
                           # height=750,
                           # width=600,
                           # title='Density map of West Nile Virus if all trap area were NOT sprayed'
                           # ),
              #row=1, col=1)

#fig.add_trace(px.density_mapbox(spray_df, 
                           # lat='Latitude', 
                           # lon='Longitude', 
                          #  z='WnvPresent', 
                           # animation_frame='Date',
                          #  zoom=9,
                          #  height=750,
                          #  width=600,
                          #  title='Density map of West Nile Virus if all trap area were ALL sprayed'
                          #  ),
             # row=1, col=2)
#fig.add_trace(go.Densitymapbox(lat=no_spray_df['Latitude'], lon=no_spray_df['Longitude'], z=no_spray_df['WnvPresent'], 
                   # radius = 4,), 
             # row=1, col=1)

#fig.add_trace(go.Densitymapbox(lat=spray_df['Latitude'], lon=spray_df['Longitude'], z=spray_df['WnvPresent'], 
                 #   radius = 4,), 
             # row=1, col=2)

#update the common attributes:
#fig.update_mapboxes(
       # accesstoken=mapboxt,
       # center=dict(
         #   lat=41.85,
         #   lon=-87.7
       # ))
   
#update different styles:
#fig.update_layout(mapbox_style="carto-positron", mapbox2_style="carto-positron")

#fig.update_traces(showscale=False) # removes default color scale on the side

#st.plotly_chart(fig, use_container_width=False) 


