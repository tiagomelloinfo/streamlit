import pandas as pd
import streamlit as st
from pycaret.classification import load_model, predict_model

def bank_churn():
    st.title('Modelo para prever CHURN')
    st.markdown('''
    <a href="https://github.com/tiagomelloinfo/estudos_machine_learning/blob/main/lgb_churn_v1.ipynb" target="_blank">
        <button>Notebook do projeto</button>
    </a>
    ''', unsafe_allow_html = True)
    st.write('\n')
    st.write('\n')
    st.write('''
    Esse modelo prevê a probabilidade da evasão de cliente para um banco
    e informa o score onde quanto mais próximo de 1000, maior a chance
    de evasão.
    ''')

    st.markdown('---')
    ###
    idade = st.number_input('Idade', min_value=18, max_value=90, value=30)
    genero = st.selectbox('Sexo', ['Masculino', 'Feminino'])
    dependentes = st.number_input('Dependentes', min_value=0, max_value=5, value=0)
    educacao = st.selectbox('Sexo', [
        'Fundamental Incompleto',
        'Fundamental Completo'
        'Médio Completo',
        'Graduação completa',
        'Pós-graduado | Mestrado completo',
        'Doutorado completo',
        'Outros'
    ])
    estado_civil = st.selectbox('Estado Civil', ['Solteiro', 'Casado', 'Divorciado', 'Outros'])
    salario = st.selectbox('Renda Anual', [
        '$60K - $80K', 'Less than $40K', 
        '$80K - $120K', '$40K - $60K',
        '$120K +', 'Unknown'
    ])
    cartao = st.selectbox('Tipo de Cartão', ['Blue', 'Gold', 'Silver', 'Platinum'])
    meses = st.number_input('Meses como Cliente', min_value=1, max_value=100, value=1)
    produtos = st.slider('Quantidade de Proutos', min_value=1, max_value=10, value=1)
    inatividade_12 = st.number_input('Meses de inatividade nos últimos 12 meses', min_value=0, max_value=12, value=0)
    contatos_12 = st.number_input('Quantidade de contatos nos últimos 12 meses', min_value=0, max_value=36, value=0)
    credit_limit = st.number_input('Limite no cartão de crédito', min_value=1000, max_value=100000, value=5000)
    saldo_retroativo = st.number_input('Saldo disponivel no cartão de crédito', min_value= 0, max_value=100000, value=0)
    linha_credito_12 = st.number_input('Aumento de Limite nos últimos 12 meses', min_value=0, max_value=10000, value=100)
    valor_entre_transacoes = st.number_input('Alteração de valor entre transações [Q4 - Q1]', min_value=0, max_value=4, value=0)
    valor_transacao_12 = st.number_input('Valor total de transações nos últimos 12 meses', min_value=0, max_value=120000, value=0)
    qt_transacao = st.number_input('Quantidade de transações', min_value=0, value=0)
    qt_transacao_quartil = st.number_input('Quantidade de transações [Q1 - Q4]', min_value=0, max_value=4, value=0)
    tx_media_uso = st.number_input('Taxa média de uso do cartão (%)', min_value=0, max_value=100, value=0)*0.001

    ###
    educacao_dict = {
        'Fundamental Incompleto': 'Uneducated',
        'Fundamental Completo': 'College',
        'Médio Completo': 'High School',
        'Graduação completa': 'Graduate',
        'Pós-graduado | Mestrado completo': 'Post-Graduate',
        'Doutorado completo': 'Doctorate',
        'Outros': 'Unknown'
    }
    maritial_dict = {
        'Solteiro': 'Single',
        'Casado': 'Married',
        'Divorciado': 'Divorced',
        'Outros': 'Unknown'
    }

    st.markdown('---')
    ###
    if st.button('EXECUTAR MODELO'):
        dados = {
            'Customer_Age': idade,
            'Gender': genero[0],
            'Dependent_count': dependentes,
            'Education_Level': educacao_dict.get(educacao),
            'Marital_Status': maritial_dict.get(estado_civil),
            'Income_Category': salario,
            'Card_Category': cartao,
            'Months_on_book': meses,
            'Total_Relationship_Count': produtos,
            'Months_Inactive_12_mon': inatividade_12,
            'Contacts_Count_12_mon': contatos_12,
            'Credit_Limit': credit_limit,
            'Total_Revolving_Bal': saldo_retroativo,
            'Avg_Open_To_Buy': linha_credito_12,
            'Total_Amt_Chng_Q4_Q1': valor_entre_transacoes,
            'Total_Trans_Amt': valor_transacao_12,
            'Total_Trans_Ct': qt_transacao,
            'Total_Ct_Chng_Q4_Q1': qt_transacao_quartil,
            'Avg_Utilization_Ratio': tx_media_uso
        }

        dados = pd.DataFrame([dados])
        modelo = load_model('./ml_models/lgb_churn_v1')
        churnscore = predict_model(modelo, dados, raw_score=True)['Score_Attrited Customer'][0]
        st.write(f'O churnscore é de {int(churnscore*1000)}')
