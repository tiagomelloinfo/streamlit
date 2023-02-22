import streamlit as st
from datetime import date, datetime

from settings import Settings

from paginas.modelos_saude import reg_precificacao_saude, smoker_fraud
from paginas.home import home

settings = Settings()
paginas = settings.paginas

st.sidebar.write('## MENU')
pagina_selecionada = st.sidebar.radio('', paginas)

if pagina_selecionada == paginas[0]:
    home()

if pagina_selecionada == paginas[1]:
    reg_precificacao_saude()

if pagina_selecionada == paginas[2]:
    smoker_fraud()
