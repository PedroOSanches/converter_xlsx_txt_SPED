import pandas as pd
from pandas import DataFrame
from typing import List, Dict
from collections.abc import Callable


from ..services.formatador_dataframe import FormatadorDataFrame
from ..enums.tipo_de_formatacao_enum import TipoFormatacao, ConfigFormatacoes


class ConcatenadorDataFrames:

    def concatena_dataframes(
        self,
        dataframes: list[DataFrame],
        config: ConfigFormatacoes
    ) -> DataFrame:

        df = pd.concat(
            dataframes,
            ignore_index=True
        )

        return self.agrupa_dataframe(df, config)


    def agrupa_dataframe(
        self,
        dataframe: DataFrame,
        config: ConfigFormatacoes
    ) -> DataFrame:

        if config.coluna_chave is None:
            return dataframe

        colunas_soma = config.colunas_soma or set()

        agregacoes = {
            coluna: (
                "sum"
                if coluna in colunas_soma
                else "first"
            )
            for coluna in dataframe.columns
            if coluna != config.coluna_chave
        }

        dataframe = (
            dataframe
            .groupby(config.coluna_chave, as_index=False)
            .agg(agregacoes)
        )

        for funcao in (config.colunas_recalcular or {}).values():
            dataframe = funcao(dataframe)

        if config.ordem_colunas:
            dataframe = FormatadorDataFrame.reordena_dataframe(
                dataframe,
                config.ordem_colunas
            )

        return dataframe