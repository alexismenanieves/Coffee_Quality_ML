import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px

df = pd.read_csv('../data/final/coffee_model_final.csv')

st.title('Coffee Analysis')
fig_sm = px.scatter_matrix(df, dimensions=['aroma','aftertaste','acidity'], color='specialty')
st.plotly_chart(fig_sm)