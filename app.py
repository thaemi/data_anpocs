import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.text(" Plataforma Teste para projeto 'data.(Anpocs).' ")
st.text('protótipo 0.0.0.1')

st.title("Boas vindas ao")
st.image("projeto.py/1.png", width=200)
st.title('Trabalhos armazenados pelo data.(Anpocs)')

trabalhos = pd.read_excel('trabalhos.py.xlsx')

lista_dos_trabalhos = trabalhos['Tema do GT'].unique()

lista_dos_trabalhos = np.append(lista_dos_trabalhos, '')

lista_dos_trabalhos.sort()

selecao = st.sidebar.selectbox('', lista_dos_trabalhos)

if selecao == 'Gênero, Trabalho e família':
  st.header("Esses são os trabalhos do tema 'Gênero, Trabalho e família' ")
  st.markdown("- As desigualdades nas narrativas de homens e mulheres no ABC paulista: gênero, família e trabalho")
  st.markdown("- Antigos habitus, novos direitos: a persistente desigualdade no trabalho doméstico")
  st.markdown("- Trabalho e família no campo da tecnologia da informação: as desigualdades persistem?")
  st.write("[link] (http://anpocs.org/index.php/encontros/papers/41-encontro-anual-da-anpocs/gt-30/gt13-17)")
  

if selecao == 'O Rural no Brasil contemporâneo: questões teóricas e novos temas de pesquisa' :
  st.header("Esses são os trabalhos do tema 'O Rural no Brasil contemporâneo: questões teóricas e novos temas de pesquisa")
  st.markdown("Dinâmica da população e produção de commodities: desigualdades socioespaciais no rural paulista")  
  st.write("[link] (http://anpocs.org/index.php/encontros/papers/41-encontro-anual-da-anpocs/gt-30/gt19-26")
  
if selecao == 'Controles Democráticos: Instituições e participação na democracia contemporânea':
  st.header("Esses são os trabalhos do tema 'Controles Democráticos: Instituições e participação na democracia contemporânea' ")
  
  st.markdown("Instituições Participativas, Desigualdades Sociais e Democracia")
  st.write("[link] (https://www.anpocs.com/index.php/papers-40-encontro-3/gt-31/gt07-16/11164-instituicoes-participativas-desigualdades-sociais-e-democracia/file")
  st.markdown("Controles Democráticos: Instituições e participação na democracia contemporânea")
  st.write("[link] (https://anpocs.com/index.php/papers-38-encontro/gt-1/gt08-1/8889-desigualdade-na-ampliacao-das-inovacoes-participativas-caracteristicas-dos-municipios-com-orcamentos-participativos-no-brasil/file")

if selecao == 'As classes sociais no Brasil contemporâneo':
  st.header("Esses são os trabalhos do tema 'As classes sociais no Brasil contemporâneo' ")

if selecao == 'Democracia e desigualdades':
  st.header("Esses são os trabalhos do tema 'Democracia e desigualdades' ")

if selecao == 'Políticas públicas':
  st.header("Essess são os trabalhos do tema 'Políticas públicas' ")
  
            
st.write('fale conosco:')
st.image("projeto.py/logo.twitter.png", width=50)
st.image("projeto.py/logo.instagram.png", width=50)
st.image("projeto.py/logo.email.jpg", width=50)
            
            
            
            
