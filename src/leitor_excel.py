import pandas as pd
from pandas import DataFrame
from typing import Tuple, Literal, Dict

class LeitorExcel:

    def obter_dataframes(self, arquivos: Tuple[str, ...] | Literal['']) -> Dict[str, DataFrame]:
        dicionario_arquivos: Dict[str, DataFrame] = {}
        for arquivo in arquivos:
            nome_arquivo = arquivo.split("/")[-1]
            dicionario_arquivos.update({nome_arquivo: pd.read_excel(arquivo)})
        return dicionario_arquivos