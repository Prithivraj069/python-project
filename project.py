import streamlit as st
import pandas as pd
import plotly.express as px


st.title("Data Visualization")

dataframe = pd.read_csv("sales_records.csv")
st.sidebar.write("Filter By")
Categories = dataframe['category'].unique().tolist()
selected_Categories = st.sidebar.multiselect("Select Categories", Categories)
st.write("User has selected", selected_Categories)


if selected_Categories:
    filter = dataframe['category'].isin(selected_Categories)
    dataframe_filter = dataframe[filter]
else:
    dataframe_filter = dataframe

st.dataframe(dataframe_filter)

if selected_Categories:
    fig = px.box(dataframe_filter, x="category", y="price",
    labels= {'category': 'Categories', 'price': 'Sales'},
    title="Price Distribution")
    
    st.plotly_chart(fig)

