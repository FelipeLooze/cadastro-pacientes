# Cadastro de Pacientes

Atividade de comparação entre Gradio e Streamlit, com gravação em CSV.

## Executar

Na pasta do projeto, instale as bibliotecas:

```powershell
python -m pip install -r requirements.txt
```

Gradio:

```powershell
python gradio_app/app.py
```

Streamlit:

```powershell
python -m streamlit run streamlit_app/app.py
```

Cada aplicativo cria um pacientes.csv na sua pasta. No Streamlit, a tabela e o download
mostram os dados da sessão atual. O CSV no servidor recebe todos os cadastros,
mas é temporário na nuvem. Use o download antes de sair.
