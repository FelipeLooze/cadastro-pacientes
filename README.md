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

O pacientes.csv na raiz contém exemplos fictícios. Não é carregado pelos aplicativos.
A tabela exibe os últimos cinco registros.

## Publicar

Envie o projeto para o GitHub. Em share.streamlit.io, selecione o repositório,
a branch main e o arquivo streamlit_app/app.py. Use Python 3.12.
Após publicar, teste o cadastro e o download também no celular.
