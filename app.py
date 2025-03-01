import streamlit as st
import pandas as pd

def carregar_arquivo(uploaded_file):
    """Carrega um arquivo CSV ou Parquet e retorna um DataFrame."""
    if uploaded_file is not None:
        if uploaded_file.name.endswith(".csv"):
            return pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith(".parquet"):
            return pd.read_parquet(uploaded_file)
        else:
            st.error("Formato de arquivo não suportado. Envie um CSV ou Parquet.")
    return None

# Configuração inicial do Streamlit
st.title("Data Cleaner & Analyzer")
st.write("Envie seu arquivo para análise de dados, limpeza e comparação.")

# Upload de arquivo
uploaded_file = st.file_uploader("Envie um arquivo CSV ou Parquet", type=["csv", "parquet"])

df = carregar_arquivo(uploaded_file)

if df is not None:
    st.write("## Visualização dos Dados")
    st.dataframe(df.head())
