import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.text(" Plataforma Teste para projeto 'data.(Anpocs).' ")
st.text('protótipo 0.0.0.1')

st.title("Boas vindas ao")
st.image("projeto.py/1.png", width=200)
st.title('Trabalhos armazenados pelo data.(Anpocs).')

trabalhos = pd.read_excel('trabalhos.py.xlsx')

lista_dos_trabalhos = trabalhos['Tema do GT'].unique()

lista_dos_trabalhos = np.append(lista_dos_trabalhos, '')

lista_dos_trabalhos.sort()

selecao = st.sidebar.selectbox('', lista_dos_trabalhos)

if selecao == 'Gênero, Trabalho e família':
  st.header("Esses são os trabalhos do tema 'Gênero, Trabalho e família' ")
  st.write("[link] (http://anpocs.org/index.php/encontros/papers/41-encontro-anual-da-anpocs/gt-30/gt13-17)")
  
  st.markdown("As desigualdades nas narrativas de homens e mulheres no ABC paulista: gênero, família e trabalho")
  
  
  st.markdown("Antigos habitus, novos direitos: a persistente desigualdade no trabalho doméstico")
  
  st.markdown("Trabalho e família no campo da tecnologia da informação: as desigualdades persistem?")
  

if selecao == 'O Rural no Brasil contemporâneo: questões teóricas e novos temas de pesquisa' :
  st.header("Esses são os trabalhos do tema 'O Rural no Brasil contemporâneo: questões teóricas e novos temas de pesquisa' ")
 
if selecao == 'Controles Democráticos: Instituições e participação na democracia contemporânea':
  st.header("Esses são os trabalhos do tema 'Controles Democráticos: Instituições e participação na democracia contemporânea' ")

if selecao == 'As classes sociais no Brasil contemporâneo':
  st.header("Esses são os trabalhos do tema 'As classes sociais no Brasil contemporâneo' ")

if selecao == 'Democracia e desigualdades':
  st.header("Esses são os trabalhos do tema 'Democracia e desigualdades' ")

if selecao == 'Políticas públicas':
  st.header("Essess são os trabalhos do tema 'Políticas públicas' ")
  
            
st.write('fale conosco:')
st.image("projeto.py/logo.twitter.png", width=50)
            
            
            
            
            
            
