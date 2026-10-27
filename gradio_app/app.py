from datetime import datetime
from pathlib import Path

import gradio as gr
import pandas as pd

ARQUIVO_CSV = Path(__file__).with_name("pacientes.csv")
COLUNAS = ["timestamp", "nome", "idade", "convenio", "prioridade", "motivo"]
CONVENIOS = ["Particular", "Unimed", "Bradesco Saúde", "SulAmérica", "Outro"]


def ultimos_cadastros():
    if ARQUIVO_CSV.exists() and ARQUIVO_CSV.stat().st_size > 0:
        return pd.read_csv(ARQUIVO_CSV, keep_default_na=False).tail(5)
    return pd.DataFrame(columns=COLUNAS)


def cadastrar_paciente(nome, idade, convenio, prioridade, motivo):
    if not nome.strip():
        return "Informe o nome do paciente.", ultimos_cadastros()
    if idade is None or not 0 <= idade <= 120 or idade != int(idade):
        return "Informe uma idade inteira entre 0 e 120.", ultimos_cadastros()

    linha = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "nome": nome.strip(),
        "idade": int(idade),
        "convenio": convenio,
        "prioridade": int(prioridade),
        "motivo": motivo.strip(),
    }

    # Grava o cabeçalho apenas no primeiro cadastro.
    novo_arquivo = not ARQUIVO_CSV.exists() or ARQUIVO_CSV.stat().st_size == 0
    pd.DataFrame([linha], columns=COLUNAS).to_csv(
        ARQUIVO_CSV, mode="a", header=novo_arquivo, index=False, encoding="utf-8-sig"
    )
    return "Paciente cadastrado com sucesso!", ultimos_cadastros()


with gr.Blocks(title="Cadastro de Pacientes") as demo:
    gr.Markdown("# Cadastro de Pacientes")
    nome = gr.Textbox(label="Nome do paciente")
    idade = gr.Number(label="Idade", minimum=0, maximum=120, precision=0, value=0)
    convenio = gr.Dropdown(CONVENIOS, label="Convênio", value="Particular")
    prioridade = gr.Slider(1, 5, step=1, value=1, label="Prioridade do atendimento", info="5 = urgente")
    motivo = gr.Textbox(label="Motivo da consulta / observações", lines=3)
    botao = gr.Button("Cadastrar")
    mensagem = gr.Textbox(label="Status", interactive=False)
    tabela = gr.Dataframe(label="Últimos cadastros", headers=COLUNAS, interactive=False)

    botao.click(
        cadastrar_paciente,
        inputs=[nome, idade, convenio, prioridade, motivo],
        outputs=[mensagem, tabela],
    )
    demo.load(ultimos_cadastros, outputs=tabela)

if __name__ == "__main__":
    demo.launch()
