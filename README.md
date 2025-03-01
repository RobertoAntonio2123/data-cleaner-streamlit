# Data Cleaner Streamlit

## Descrição

O **Data Cleaner Streamlit** é uma aplicação interativa desenvolvida em **Python** usando **Streamlit**. Ele permite:

- **Limpeza de dados** (remoção de duplicatas, tratamento de valores nulos, padronização)
- **Filtragem e agrupamento**
- **Junção de múltiplas tabelas**
- **Comparação de tabelas** (diferenças entre arquivos, entradas e saídas, análise de linhas removidas e adicionadas)
- **Exportação de resultados** em **CSV** ou **Parquet**

## Instalação

1. **Clone este repositório:**
   ```sh
   git clone https://github.com/RobertoAntonio2123/data-cleaner-streamlit.git
   cd data-cleaner-streamlit
   ```

2. **Crie e ative um ambiente virtual com Miniconda:**
   ```sh
   conda create --name data_cleaner_env python=3.10 -y
   conda activate data_cleaner_env
   ```

3. **Instale as dependências:**
   ```sh
   pip install -r requirements.txt
   ```

## Como Executar

1. Navegue até a pasta do projeto:
   ```sh
   cd caminho/para/data-cleaner-streamlit
   ```

2. Execute o Streamlit:
   ```sh
   streamlit run app.py
   ```

3. Acesse a aplicação pelo navegador no endereço:
   ```
   http://localhost:8501
   ```

## Funcionalidades

### 1. **Limpeza de Dados**
- Remoção de valores nulos
- Remoção de duplicatas
- Conversão de tipos de dados

### 2. **Filtragem e Agrupamento**
- Filtrar por colunas e valores específicos
- Agrupar dados por categorias

### 3. **Junção de Tabelas**
- Combinação de duas ou mais tabelas com base em colunas comuns

### 4. **Comparação de Tabelas**
- Mostra diferenças entre duas tabelas (novas entradas, remoções e mudanças)
- Conta linhas adicionadas/removidas
- Calcula a média de valores nulos antes e depois

### 5. **Exportação de Dados**
- Exporta os dados processados para **CSV** ou **Parquet**

## Exemplo de Uso

1. **Upload de Arquivo:**
   - Faça upload de arquivos CSV ou Parquet.
   
2. **Escolha a Operação:**
   - Selecione as opções de limpeza, filtro e análise.

3. **Visualização dos Resultados:**
   - Veja a tabela tratada e as diferenças identificadas.

4. **Baixe o Arquivo:**
   - Escolha o formato desejado para exportar os dados limpos.

## Contribuição

Sinta-se à vontade para abrir issues e pull requests para melhorias!

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

