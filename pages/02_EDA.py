import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pickle
import seaborn as sns

@st.cache
def train_data(): 
    df = pd.read_csv('../train.csv')
    return df

st.container()
st.header('')
df = train_data()

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
    
st.pyplot(barplot1())
          
    
