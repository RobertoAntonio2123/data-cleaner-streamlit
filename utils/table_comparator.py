import pandas as pd

def compare_tables(df1: pd.DataFrame, df2: pd.DataFrame) -> dict:
    result = {
        "total_rows_df1": len(df1),
        "total_rows_df2": len(df2),
        "common_rows": len(pd.merge(df1, df2, how='inner')),
        "rows_only_in_df1": len(df1) - len(pd.merge(df1, df2, how='inner')),
        "rows_only_in_df2": len(df2) - len(pd.merge(df1, df2, how='inner')),
        "null_values_df1": df1.isnull().sum().mean(),
        "null_values_df2": df2.isnull().sum().mean()
    }
    return result
