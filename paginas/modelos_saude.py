import pandas as pd
import streamlit as st
from pycaret.classification import load_model, predict_model

def reg_precificacao_saude():
    st.title('SEGURO - Precificação')
    st.write('''
    Com base em alguns dados do cliente, poderá obter valor de custo do seguro, valor de lucro de acordo com a (%) margem de lucro informada
    e o valor final para cobrança.
    ''')
    
    st.markdown('---')
    age = st.number_input('Idade', min_value=18, max_value=65, value=30)
    sexo = {'Masculino': 'male', 'Feminino': 'female'}.get(st.selectbox('Sexo', ['Masculino', 'Feminino'])) 
    imc = st.number_input('Índice de Massa Corporal', min_value=15, max_value=54, value=24)
    fumante = {True: 'yes', False: 'no'}.get(st.checkbox('É fumante?'))
    criancas = st.number_input('Quantidade de Dependentes', min_value=0, max_value=5, value=0)
    regiao = {
        'Nordeste': 'northeast', 
        'Noroeste': 'northwest', 
        'Sudeste': 'southeast', 
        'Centro-oeste': 'southwest'
    }.get(st.selectbox('Região onde mora', ['Nordeste', 'Noroeste', 'Sudeste', 'Centro-oeste']))

    st.markdown('---')
    margem_lucro = st.slider('(%) Margem de lucro', min_value=0, max_value=200, value=20, step=5)

    dados = pd.DataFrame([dict(
        age = age,
        sex = sexo,
        bmi = imc,
        smoker = fumante,
        children = criancas,
        region = regiao
    )])

    st.markdown('---')

    if st.button('EXECUTAR MODELO'):
        modelo = load_model('rf_charges_v1')
        res = predict_model(modelo, dados)
        valor_cobranca = res['Label'][0]
        valor_lucro = int(valor_cobranca * (margem_lucro / 100))
        res = str(res['Label'][0]/1000).replace(',', '.')
        st.write(f"Custo estimado de $ {res},00")
        st.write(f"O valor de lucro será de $ {str((valor_lucro)/1000).replace(',', '.')},00")
        st.write(f"O valor de cobrança deve ser de $ {str((valor_cobranca + valor_lucro)/1000).replace(',', '.')},00")


def smoker_fraud():
    st.title('SEGURO - Fraude')
    st.write('''
    Existem informações que são relevantes na hora de precificar um seguro e algumas delas possuem um peso maior,
    que é o caso de pessoas fumantes alegando não serem fumantes para reduzir o valor final.

    Com base em alguns dados, podemos avaliar qual a chance de um cliente ser fumante, com base no conceito de "score"
    de 0 a 100.
    ''')
    st.markdown('---')
    age = st.number_input('Idade', min_value=18, max_value=65, value=30)
    sexo = {'Masculino': 'male', 'Feminino': 'female'}.get(st.selectbox('Sexo', ['Masculino', 'Feminino'])) 
    imc = st.number_input('Índice de Massa Corporal', min_value=15, max_value=54, value=24)
    custos = st.number_input('Custos', min_value=1000, max_value=50000, value=10000)
    criancas = st.number_input('Quantidade de Dependentes', min_value=0, max_value=5, value=0)
    regiao = {
        'Nordeste': 'northeast', 
        'Noroeste': 'northwest', 
        'Sudeste': 'southeast', 
        'Centro-oeste': 'southwest'
    }.get(st.selectbox('Região onde mora', ['Nordeste', 'Noroeste', 'Sudeste', 'Centro-oeste']))

    dados = pd.DataFrame([dict(
        age = age,
        sex = sexo,
        bmi = imc,
        charges = custos,
        children = criancas,
        region = regiao
    )])

    st.markdown('---')

    if st.button('EXECUTAR MODELO'):
        modelo = load_model('bagging_classifier_fraud_smoker_v1')
        res = predict_model(modelo, dados, raw_score=True)
        pronome = 'o' if sexo == 'male' else 'a'
        probabilidade = int(res['Score_yes'][0] * 100)
        st.write(f'A probabilidade d{pronome} cliente ser fumante é de {probabilidade}%')

