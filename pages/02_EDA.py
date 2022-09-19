import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pickle

@st.cache
def train_data(): 
    df = pd.read_csv('../train.csv')
    return df

st.container()
st.header(')
