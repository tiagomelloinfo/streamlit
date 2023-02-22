import streamlit as st

def home():
    st.title('Tiago Mello')
    st.header('CIENTISTA DE DADOS')

    st.markdown('---')
    st.write('## CONTATOS')
    st.write('tiagomello.ds@gmail.com')
    st.markdown('''
    <a href="https://wa.me/5521989669097" target="_blank">
        Whatsapp
    </a>
    ''', unsafe_allow_html = True)
    st.markdown('''
    <a href="https://www.linkedin.com/in/tiagomello-datascientist/" target="blank">
        Linkedin
    </a>
    ''', unsafe_allow_html = True)

    st.markdown('---')
    st.write('## RESUMO')
    st.write('''
    Olá, tudo bem?

    Seja bem vindo(a) ao meu perfil!

    Sou Tiago Mello, e desde a adolescência sigo a tendência de tomar decisões baseadas em dados de forma quase insintiva.

    Há mais de 10 anos, trabalho com auxílio em tomadas de decisões baseadas em dados, com uso de tecnologias e ferramentas como Excel e Python. 

    Participei de projetos com squads interdisciplinares para trabalhar com grandes fluxos de dados, pipelines e modelagem preditiva com uso de SQL, Docker, API, Python e Sci-kit Learn.

    Tenho experiência com monitoramento de padrões e tendências, entendendo o momento atual e prevendo mutações para planejar novas estratégias com o melhor tempo de resposta.

    Faço uso de ferramentas como Telegram e PowerBI para criar alertas e gerar relatórios analíticos gerenciais e admnistrativos para acompanhar resultados e ajudar a prever mudanças nas tendências, o que deixa as tomadas de decisões mais precisas.

    Atuei em diversas frentes como risco, crédito, fraude e experiência do cliente B2B, B2C e B2B2C.

    Graduação em Ciência de Dados prevista para final de março de 2023, com pretensão de iniciar o MBA em Inteligência artificial no segundo semestre.
    
    ''')

    st.markdown('---')
    st.write('## EXPERIÊNCIAS')

    st.write('''
    **CIENTISTA DE DADOS** na VirtusPay (Novembro de 2020 - Setembro de 2022)

    - Desenvolvimento e de modelos preditivos (machine learning) com aplicação de pipeline para melhorar a assertividade em criar creditscore e fraudscore para clientes.
    
    - Desenvolvimento pipeline de dados através de Scripts em Python e SQL para popular tabelas de data warehouse que servem para visualizações em dashboards que monitoram tendências.
    
    - Criação de relatórios interativos com ferramentas de visualização, para acompanhar mudanças de tendências.
    
    - Criação de relatórios interativos com ferramenta de visualização, para acompanhar a produtividade dos modelos preditivos, com visualização de seus resultados e variáveis usadas.
    
    - Trabalho em conjunto com equipes de estratégia para redução no risco de crédito e fraude.
    
    - Validação de backtest referente a novos parceiros sobre o impacto nos negócios, em teste de possível contrato.


    **DESENVOLVEDOR E CIENTISTA DE DADOS** Autônomo (Junho de 2018 - Novembro de 2020)

    - Desenvolvimento e manutenção de API microsservice para melhorar performance e reduzir consumo de recursos.

    - Desenvolvimento e aplicação de pipeline de modelos de machine learn através de API REST.

    - Aumento de segurança dos dados para trafegar pelo sistema.

    - Criação de monitoria de erros e bugs em tempo real para melhorar o tempo de resposta para correção dos mesmos.

    - Criação de dashboards gerenciais e administrativos para auxiliar nas tomadas de decisão.

    - Desenvolvimento de API para decisões automáticas e semi-automáticas para reduzir filas de espera e tempo de resposta ao cliente.
    ''')
