import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.markdown("Boas vindas ao")
st.image("projeto.py/1.png")
st.title('data.(Anpocs)!')
st.text('protótipo 1.0')
st.text('ola, ola, ola')
st.write('fale conosco: redes sociais')

trabalhos = pd.read_excel('trabalhos.py.xlsx')

lista_dos_trabalhos = trabalhos['Tema do GT'].unique()

lista_dos_trabalhos = np.append(lista_dos_trabalhos, '')

lista_dos_trabalhos.sort()

selecao = st.sidebar.selectbox('', lista_dos_trabalhos)

if selecao == 'Gênero, Trabalho e família':
  st.header("Esses são os trabalhos do tema 'Gênero, Trabalho e família' ")
  
if selecao == 'O Rural no Brasil contemporâneo: questões teóricas e novos temas de pesquisa' :
  st.header("Esses são os trabalhos do tema 'O Rural no Brasil contemporâneo: questões teóricas e novos temas de pesquisa' ")
 
if selecao == 'Controles Democráticos: Instituições e participação na democracia contemporânea':
  st.header("Esses são os trabalhos do tema 'Controles Democráticos: Instituições e participação na democracia contemporânea' ")

if selecao == 'As classes sociais no Brasil contemporâneo':
  st.header("Esses são os trabalhos do tema 'As classes sociais no Brasil contemporâneo' ")

if selecao == 'Controles Democráticos: Participação Política: atores,instituições, dinâmicas e resultados':
  st.header("Esses são os trabalhos do tema 'Controles Democráticos: Participação Política: atores,instituições, dinâmicas e resultados' ")

            
            
            
            
            
            
            
            
