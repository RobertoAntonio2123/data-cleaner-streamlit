import streamlit as st
import pandas as pd
import os
import re
from collections import Counter
from utils.file_handler import load_data

st.set_page_config(page_title="Leitor de CSV", layout="wide")

st.title("📂 Leitor de Arquivos CSV")

uploaded_file = st.file_uploader("Escolha um arquivo CSV (até 600MB)", type=["csv"])

if uploaded_file is not None:
    # Obtém o tamanho do arquivo em MB
    uploaded_file.seek(0, os.SEEK_END)
    file_size_mb = uploaded_file.tell() / (1024 * 1024)
    uploaded_file.seek(0)  # Retorna ao início do arquivo

    try:
        df = load_data(uploaded_file)

        # Obtém o número de linhas e colunas
        num_linhas, num_colunas = df.shape

        # Exibe tudo na mesma linha
        st.write(
            f"✅ **Arquivo carregado com sucesso!** Tamanho: **{file_size_mb:.2f} MB** | "
            f"📊 **O arquivo contém {num_linhas:,} linhas e {num_colunas} colunas**"
        )

        # Exibe as primeiras 10 linhas do DataFrame
        st.dataframe(df.head(10))

        # Layout lado a lado
        col1, col2, col3 = st.columns(3)

        with col1:
            st.write("📉 **Estatísticas de dados nulos por coluna**")
            missing_values = df.isnull().sum()
            missing_percentage = (missing_values / num_linhas) * 100
            st.dataframe(pd.DataFrame({
                "Valores Nulos": missing_values,
                "Porcentagem (%)": missing_percentage
            }))

        with col2:
            st.write("🔁 **Porcentagem de valores duplicados por coluna**")
            duplicated_percentage = df.apply(lambda x: x.duplicated().sum() / num_linhas * 100)
            st.dataframe(pd.DataFrame({"Duplicados (%)": duplicated_percentage}))

        # 🔥 RANKING DAS PALAVRAS MAIS REPETIDAS 🔥
        def contar_palavras(df):
            texto = " ".join(df.astype(str).stack())  # Junta todo o conteúdo do DataFrame
            palavras = re.findall(r'\b\w+\b', texto.lower())  # Divide em palavras
            palavras_ignoradas = {"de", "da", "do", "e", "a", "o", "os", "as", "um", "uma", "para"}  # Remove palavras irrelevantes
            palavras_filtradas = [p for p in palavras if p not in palavras_ignoradas]
            return Counter(palavras_filtradas).most_common(10)  # Retorna as 10 palavras mais comuns

        ranking_palavras = contar_palavras(df)

        # Encontrar em quais colunas essas palavras aparecem mais
        def colunas_mais_frequentes(df, palavras_top):
            colunas_por_palavra = {}
            for palavra, _ in palavras_top:
                contagens = df.apply(lambda col: col.astype(str).str.contains(fr"\b{palavra}\b", case=False, regex=True).sum())
                coluna_mais_frequente = contagens.idxmax()  # Pega a coluna com mais ocorrências
                colunas_por_palavra[palavra] = coluna_mais_frequente
            return colunas_por_palavra

        colunas_repetidas = colunas_mais_frequentes(df, ranking_palavras)

        # Criar DataFrame final
        df_ranking = pd.DataFrame(ranking_palavras, columns=["Palavra", "Frequência"])
        df_ranking["Coluna mais frequente"] = df_ranking["Palavra"].map(colunas_repetidas)

        with col3:
            st.write("📊 **Ranking das palavras mais repetidas e colunas mais afetadas**")
            st.dataframe(df_ranking)

    except Exception as e:
        st.error(f"⚠️ Erro ao carregar o arquivo: {e}")
