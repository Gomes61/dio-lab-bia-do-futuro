import json 
import streamlit as st 
import pandas as pd
import requests

# ============ CONFIGURAÇÃO ============
OLLAMA_URL = "http://localhost: 11434/api/generate"
MODELO = "gemma3:1b"

# ============ CARREGAR DADOS ============
perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

# ============ MONTAR CONTEXTO ============ 
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES: 
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS: 
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# ============ MONTAR CONTEXTO ============ 
SYSTEM_PROMPT = """Você é o Mar , um educador financeiro didático e informativo. 
OBJETIVO:
Seu papel é ensinar conceitos financeiros de forma clara, didática e estruturada, ajudando as pessoas a entenderem como administrar dinheiro, poupar, investir e interpretar informações econômicas.

REGRAS:
- Sempre baseie suas respostas nos dados fornecidos pelo usuário ou em princípios financeiros reconhecidos;
- Nunca invente informações financeiras, números, taxas ou dados de mercado;
- Se dados específicos forem necessários, peça ao usuário ou explique de forma conceitual;
- Se não houver algo ou não houver dados suficientes, admita claramente limitações e apresente caminhos alternativos, como: explicar o conceito explicando onde encontrar a informação mostrar como calcular ou analisar;
- Seu foco é exclusivamente educacional;
- Resposta de forma sucinta e breve com no máximo 3 parágrafos na resposta.
"""

# ============ CHAMAR OLLAMA  ============ 
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

CONTEXTO DO CLIENTE:
{contexto}

Pergunta: {msg}"""
    
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gemma3:1b"

def perguntar(prompt):

    r = requests.post(
        OLLAMA_URL,
        json={
            "model": MODELO,
            "prompt": prompt,
            "stream": False
        }
    )

    return r.json()['response']

# ============ INTERFACE ============ 
st.title(" MAR, Seu Educador Financeiro")

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))

        
