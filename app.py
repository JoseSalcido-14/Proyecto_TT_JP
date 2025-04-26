import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv('/Users/josepacheco/Documents/TripleTen DA/Modulo 2/Sprint 7 - Herramientas de desarrollo de software/Proyecto/Proyecto_TT_JP/notebooks/vehicles_us.csv')
hist_button = st.button('Construir histograma') #boton
scat_button = st.button('Construir grafico de dispersion')

st.title('Analisis de vehiculos')
st.header('KM de los vehiculos')

if hist_button:
    st.write('Creacion de un histograama para el conjunto')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

if scat_button:
    st.write('Grafico de dispersion')
    scatter = px.scatter(car_data, x='odometer', y='price', title = 'Precio vs KM')
    st.plotly_chart(scatter)