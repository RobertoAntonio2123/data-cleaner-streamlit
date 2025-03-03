import pandas as pd

def load_data(file):
    """Carrega um CSV com encoding correto e tratamento de separadores."""
    try:
        file.seek(0)  # Retorna ao início do arquivo
        
        return pd.read_csv(
            file, 
            encoding="ISO-8859-1",  # Corrige caracteres especiais
            sep=";",  # Usa ponto e vírgula como separador
            quotechar='"',  # Garante que textos entre aspas sejam lidos corretamente
            low_memory=False,  # Evita problemas com arquivos grandes
            dtype=str  # Mantém os dados como string para evitar erros de conversão
        )

    except Exception as e:
        raise Exception(f"Erro ao carregar arquivo: {e}")
