import pandas as pd
import streamlit as st
from pycaret.classification import load_model, predict_model

def credit_card_fraud():
    st.title('Modelo para prever Fraude')
    st.markdown('''
    <a href="https://github.com/tiagomelloinfo/estudos_machine_learning/blob/main/et_fraudscore_v1.ipynb" target="_blank">
        <button>Notebook do projeto</button>
    </a>
    ''', unsafe_allow_html = True)
    st.write('\n')
    st.write('\n')
    st.write('''
    Esse modelo foi treinado a partir de um conjunto de dados de cartões de crédito europeus.
    Os valores de entrada originais foram protegidos por razões de segurança, sendo eles de
    V1 até V28, além de Time (segundos após a transação anterior) e Amount (valor da transação).

    Treinado com Extra Decision Tree Classifier, o modelo pode prever com acertividade aproximada
    de 97% se a probabilidade da transação ser fraude, em uma escala de zero a mil.
    ''')

    st.markdown('---')
    min = -100
    max = 100
    v1 = st.slider('V1', min_value = min, max_value = max, value=0, step=5)
    v2 = st.slider('V2', min_value = min, max_value = max, value=0, step=5)
    v3 = st.slider('V3', min_value = min, max_value = max, value=0, step=5)
    v4 = st.slider('V4', min_value = min, max_value = max, value=0, step=5)
    v5 = st.slider('V5', min_value = min, max_value = max, value=0, step=5)
    v6 = st.slider('V6', min_value = min, max_value = max, value=0, step=5)
    v7 = st.slider('V7', min_value = min, max_value = max, value=0, step=5)
    v8 = st.slider('V8', min_value = min, max_value = max, value=0, step=5)
    v9 = st.slider('V9', min_value = min, max_value = max, value=0, step=5)
    v10 = st.slider('V10', min_value = min, max_value = max, value=0, step=5)
    v11 = st.slider('V11', min_value = min, max_value = max, value=0, step=5)
    v12 = st.slider('V12', min_value = min, max_value = max, value=0, step=5)
    v13 = st.slider('V13', min_value = min, max_value = max, value=0, step=5)
    v14 = st.slider('V14', min_value = min, max_value = max, value=0, step=5)
    v15 = st.slider('V15', min_value = min, max_value = max, value=0, step=5)
    v16 = st.slider('V16', min_value = min, max_value = max, value=0, step=5)
    v17 = st.slider('V17', min_value = min, max_value = max, value=0, step=5)
    v18 = st.slider('V18', min_value = min, max_value = max, value=0, step=5)
    v19 = st.slider('V19', min_value = min, max_value = max, value=0, step=5)
    v20 = st.slider('V20', min_value = min, max_value = max, value=0, step=5)
    v21 = st.slider('V21', min_value = min, max_value = max, value=0, step=5)
    v22 = st.slider('V22', min_value = min, max_value = max, value=0, step=5)
    v23 = st.slider('V23', min_value = min, max_value = max, value=0, step=5)
    v24 = st.slider('V24', min_value = min, max_value = max, value=0, step=5)
    v25 = st.slider('V25', min_value = min, max_value = max, value=0, step=5)
    v26 = st.slider('V26', min_value = min, max_value = max, value=0, step=5)
    v27 = st.slider('V27', min_value = min, max_value = max, value=0, step=5)
    v28 = st.slider('V28', min_value = min, max_value = max, value=0, step=5)
    time = st.number_input('Time (Segundos)', min_value=0, max_value=200000, value=0)
    amount = st.number_input('Valor da Transação ($)', min_value=0, max_value=50000, value = 100)

    if st.button('EXECUTAR MODELO'):
        dados = dict(
            V1 = v1,
            V2 = v2,
            V3 = v3,
            V4 = v4,
            V5 = v5,
            V6 = v6,
            V7 = v7,
            V8 = v8,
            V9 = v9,
            V10 = v10,
            V11 = v11,
            V12 = v12,
            V13 = v13,
            V14 = v14,
            V15 = v15,
            V16 = v16,
            V17 = v17,
            V18 = v18,
            V19 = v19,
            V20 = v20,
            V21 = v21,
            V22 = v22,
            V23 = v23,
            V24 = v24,
            V25 = v25,
            V26 = v26,
            V27 = v27,
            V28 = v28,
            Time = time,
            Amount = amount
        )

        dados = pd.DataFrame([dados])
        modelo = load_model('./ml_models/et_fraudscore_v1')
        predito = predict_model(modelo, dados, raw_score=True)
        st.write(int(predito['Score_1'][0]*1000))