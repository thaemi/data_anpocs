import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.markdown("Boas vindas ao")
st.title('data.(Anpocs)!')
st.text('protótipo 1.0')
st.text('ola, ola, ola')
st.write('fale conosco bla bla bla')

trabalhos = pd.read_excel('trabalhos.py.xlsx')

lista_dos_trabalhos = trabalhos['Tema do GT'].unique()

lista_dos_trabalhos = np.append(lista_dos_trabalhos, '')

lista_dos_trabalhos.sort()

selecao = st.sidebar.selectbox('', lista_dos_trabalhos)

gol, gol2 = st.beta_columns([5,20])
with gol
  st.image('C:\Users\Thales\Desktop\imagens.projeto.py/1')
  with gol2:
    st.info('Logo oficial do data.(Anpocs)')
