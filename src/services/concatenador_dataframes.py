import abc
from abc import abstractmethod
import pandas as pd
from pandas import DataFrame
from typing import List, Dict
from collections.abc import Callable



from ..enums.tipo_de_formatacao_enum import TipoFormatacao


class ConcatenadorDataFrames(abc.ABC):

    def concatena_dataframes(
            self, 
            dataframes: List[DataFrame], 
            config: dict
            ):
        df_concatenado = pd.concat(dataframes, ignore_index=True)

        return self.agrupa_dataframe(df_concatenado, config)

    def agrupa_dataframe(
            self, 
            dataframe: DataFrame, 
            config: dict
            ):

        coluna_chave = config["coluna_chave"]
        colunas_soma = config["coluna_soma"]

        agregacoes = {
            coluna: (
                "sum" 
                if coluna in colunas_soma
                else "first"
            )
            for coluna in dataframe.columns
            if coluna != coluna_chave
        }

        dataframe = (
            dataframe
            .groupby(coluna_chave, as_index=False)
            .agg(agregacoes)
            )

        for coluna, funcao in config["colunas_recalcular"].items():
            dataframe = funcao(dataframe)

        return dataframe