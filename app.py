import streamlit as st
import pandas as pd
from utils.data_processing import remove_duplicates, handle_missing_values, merge_tables
from utils.file_handler import load_data, save_data
from utils.table_comparator import compare_tables

def main():
    st.title("Streamlit Data Cleaner")
    
    st.sidebar.header("Upload de Arquivos")
    uploaded_file1 = st.sidebar.file_uploader("Escolha o primeiro arquivo CSV ou Parquet", type=["csv", "parquet"])
    uploaded_file2 = st.sidebar.file_uploader("Escolha o segundo arquivo para comparação (opcional)", type=["csv", "parquet"])
    
    uploaded_file = st.file_uploader("Escolha um arquivo CSV", type=["csv"])


    if uploaded_file1:
        df1 = load_data(uploaded_file1)
        st.write("### Dados Carregados")
        st.dataframe(df1.head())

        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            st.write(df.head())


        
        # Opções de limpeza
        if st.sidebar.button("Remover Duplicatas"):
            df1 = remove_duplicates(df1)
            st.write("### Dados sem duplicatas")
            st.dataframe(df1.head())
        
        if st.sidebar.button("Preencher Valores Nulos com Média"):
            df1 = handle_missing_values(df1, strategy='mean')
            st.write("### Dados sem valores nulos")
            st.dataframe(df1.head())
        
        if uploaded_file2:
            df2 = load_data(uploaded_file2)
            comparison = compare_tables(df1, df2)
            st.write("### Comparação entre Tabelas")
            st.json(comparison)
        
        # Opção de exportação
        save_format = st.sidebar.selectbox("Escolha o formato para salvar", ["CSV", "Parquet"])
        if st.sidebar.button("Salvar Arquivo"):
            save_data(df1, save_format)
            st.success(f"Arquivo salvo como {save_format.lower()}")

if __name__ == "__main__":
    main()