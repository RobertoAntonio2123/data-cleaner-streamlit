import pandas as pd

def load_data(file):
    try:
        # Tenta detectar a codificação
        encoding = "utf-8"
        
        # Lê o CSV tratando erros de quebra de linha e delimitador
        return pd.read_csv(file, encoding=encoding, sep=None, engine="python", on_bad_lines="skip")
    
    except pd.errors.ParserError as e:
        print(f"Erro ao processar o arquivo CSV: {e}")
        return None

    except UnicodeDecodeError:
        print("Erro de codificação. Tentando com 'latin1'...")
        return pd.read_csv(file, encoding="latin1", sep=None, engine="python", on_bad_lines="skip")

    except Exception as e:
        print(f"Erro inesperado: {e}")
        return None

def save_data(df, filename="output.csv"):
    """Salva um DataFrame em um arquivo CSV."""
    try:
        df.to_csv(filename, index=False, encoding="utf-8")
        print(f"Arquivo salvo como {filename}")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")

