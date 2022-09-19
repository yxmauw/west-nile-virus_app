import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

@st.cache
def train_data(): 
    df = pd.read_csv('./train.csv', parse_dates=[0], infer_datetime_format=True)
    # set date as index
    df.set_index('Date', inplace=True)
    return df

df = train_data()

frt_container = st.container()
scd_container = st.container()

with frt_container:
    st.header('Barplots showing Top 20 Traps with highest mosquito count in respective years')

    def barplot1():
        df1 = pd.DataFrame((df.loc['2007'].groupby(['Trap','Species'])['NumMosquitos'].agg('sum')).sort_values(ascending=False)[:20]).reset_index()
        df2 = pd.DataFrame((df.loc['2009'].groupby(['Species','Trap'])['NumMosquitos'].agg('sum')).sort_values(ascending=False)[:20]).reset_index()
        df3 = pd.DataFrame((df.loc['2011'].groupby(['Species','Trap'])['NumMosquitos'].agg('sum')).sort_values(ascending=False)[:20]).reset_index()
        df4 = pd.DataFrame((df.loc['2013'].groupby(['Species','Trap'])['NumMosquitos'].agg('sum')).sort_values(ascending=False)[:20]).reset_index()

        fig, axes = plt.subplots(4, figsize=(15,20))
    
        sns.barplot(x='Trap', y='NumMosquitos', hue='Species', data=df1, ax=axes[0])
        axes[0].set_title('2007 top 20 traps with mosquitos caught', fontsize=13)
        sns.barplot(x='Trap', y='NumMosquitos', hue='Species', data=df2, ax=axes[1])
        axes[1].set_title('2009 top 20 traps with mosquitos caught', fontsize=13)
        sns.barplot(x='Trap', y='NumMosquitos', hue='Species', data=df3, ax=axes[2])
        axes[2].set_title('2011 top 20 traps with mosquitos caught', fontsize=13)
        sns.barplot(x='Trap', y='NumMosquitos', hue='Species', data=df4, ax=axes[3])
        axes[3].set_title('2013 top 20 traps with mosquitos caught', fontsize=13);
        for ax in axes: # to iterate each subplot legend position
            ax.legend(loc='upper right') 
        plt.subplots_adjust(hspace=0.24) # space between subplots
        return fig
    
    st.pyplot(barplot1())
    
          
with scd_container:
    st.header('Map showing which traps had West Nile Virus detected')
    px.set_mapbox_access_token(open('./.gitignore/.mapbox_token.txt').read())
    fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", color="WnvPresent", 
                            color_discrete_sequence=['SteelBlue','Red'],
                   zoom=9, height=650, opacity=0.3)
    fig.update_traces(marker={'color':['steelblue','red'], 'symbol':['x','circle']}, selector=dict(type='mapbox'))
    st.plotly_chart(fig, use_container_width=True)
