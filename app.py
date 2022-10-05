import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.markdown("Boas vindas ao")
st.title('data.(Anpocs)!')
st.image("projeto.py/1.png")

st.write2('Acima, vocês vêem o nosso logotipo!')

st.text('protótipo 1.0')
st.text('ola, ola, ola')
st.write('fale conosco bla bla bla')

trabalhos = pd.read_excel('trabalhos.py.xlsx')

lista_dos_trabalhos = trabalhos['Tema do GT'].unique()

lista_dos_trabalhos = np.append(lista_dos_trabalhos, '')

lista_dos_trabalhos.sort()

selecao = st.sidebar.selectbox('', lista_dos_trabalhos)


