from datetime import datetime
from pathlib import Path

import pandas as pd
import streamlit as st

ARQUIVO_CSV = Path(__file__).with_name("pacientes.csv")
COLUNAS = ["timestamp", "nome", "idade", "convenio", "prioridade", "motivo"]
CONVENIOS = ["Particular", "Unimed", "Bradesco Saúde", "SulAmérica", "Outro"]

st.set_page_config(page_title="Cadastro de Pacientes", layout="centered")
st.title("Cadastro de Pacientes")

if "pacientes" not in st.session_state:
    st.session_state.pacientes = pd.DataFrame(columns=COLUNAS)

with st.form("cadastro"):
    nome = st.text_input("Nome do paciente")
    idade = st.number_input("Idade", min_value=0, max_value=120, step=1)
    convenio = st.selectbox("Convênio", CONVENIOS)
    prioridade = st.slider("Prioridade do atendimento", 1, 5, value=1)
    st.caption("5 = urgente")
    motivo = st.text_area("Motivo da consulta / observações")
    enviado = st.form_submit_button("Cadastrar")

if enviado:
    if not nome.strip():
        st.error("Informe o nome do paciente.")
    else:
        linha = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "nome": nome.strip(),
            "idade": int(idade),
            "convenio": convenio,
            "prioridade": int(prioridade),
            "motivo": motivo.strip(),
        }
        novo = pd.DataFrame([linha], columns=COLUNAS)

        # Salva no CSV e adiciona o paciente à sessão.
        novo_arquivo = not ARQUIVO_CSV.exists() or ARQUIVO_CSV.stat().st_size == 0
        novo.to_csv(
            ARQUIVO_CSV, mode="a", header=novo_arquivo, index=False, encoding="utf-8-sig"
        )
        st.session_state.pacientes = pd.concat(
            [st.session_state.pacientes, novo], ignore_index=True
        )
        st.success("Paciente cadastrado com sucesso!")

st.subheader("Últimos cadastros")
st.dataframe(st.session_state.pacientes.tail(5), hide_index=True)

csv = st.session_state.pacientes.to_csv(index=False).encode("utf-8-sig")
st.download_button("Baixar CSV", csv, "pacientes.csv", "text/csv", on_click="ignore")
st.caption("Os dados na nuvem são temporários. Baixe o CSV antes de sair.")
