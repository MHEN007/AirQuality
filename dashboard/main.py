import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('./dashboard/main_data.csv')

st.title("Dashboard Kualitas Udara")

tab_air_index, tab_tren_udara = st.tabs(["Air Quality Index", "Pollutants Trend"])

with tab_air_index:
    st.header("Air Quality Index")
    city_air_quality = df.groupby(['station', 'air_quality']).size().reset_index(name='count')

    plt.figure(figsize=(20,10))

    sns.barplot(x='station', y='count', hue='air_quality', data=city_air_quality)
    plt.title('Air Quality Index by City')
    
    st.pyplot(plt)

    st.write("Based on NO2, SO2, O3, PM2.5, and PM10 values")


with tab_tren_udara:
    st.header("Pollutants Trend")

    selection = st.selectbox("Please choose pollutant", ['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3', 'TEMP', 'PRES'])
    year_start = st.selectbox("Please choose start year", [2013, 2014, 2015, 2016, 2017])
    year_end = st.selectbox("Please choose end year", [2013, 2014, 2015, 2016, 2017])

    filtered_data = df[(df['year'] >= 2013) & (df['year'] <= year_end)]
    plt.figure(figsize=(20, 10))
    sns.lineplot(filtered_data, x='hour', y=selection)
    plt.title(f"Trend of {selection} from 2013-{year_end}")
    st.pyplot(plt)