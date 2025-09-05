import streamlit as st
import pandas as pd


st.title("Chai Sales Dashboard")

file = st.file_uploader("Upload your sales data", type=["csv", "xlsx"])

if file:
    df= pd.read_csv(file)
    st.subheader("Sales Data")
    st.dataframe(df)
if file:
    st.subheader("Sales Summary")
    st.write(df.describe())
    st.line_chart(df['Revenue']) 

if file:
    selected_city = st.selectbox("Select City", df['City'].unique())
    df[df['City'] == selected_city]
    filtered_data = df[df['City'] == selected_city]
   