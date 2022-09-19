import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pickle

@st.cache
def train_data(): 
    with open('st_no_sprayed.pkl', 'rb') as f:
        df = pickle.load(f)
    return df

st.container()
st.header(')
