from pandas import DataFrame
from typing import List, Dict


class FormatadorDataFrame:

    def formatar_cabecalho(self, df: DataFrame) -> DataFrame:
            cabecalho: List[str] = df.columns.values.tolist()
            primeira_linha = df.iloc[0]
            df = df.iloc[1:].copy()
    
            for i in range(len(cabecalho)):
                if "TOTAL GERAL" in cabecalho[i]:
                    cabecalho[i] = primeira_linha[cabecalho[i]]
    
            df.columns = cabecalho
            return df
    
    def formatar_dataframe(self, df: DataFrame) -> DataFrame:
                df = self.formatar_cabecalho(df)
                df = df.iloc[:-5]
                return df