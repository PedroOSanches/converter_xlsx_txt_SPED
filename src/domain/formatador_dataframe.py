import pandas as pd
from pandas import DataFrame
from typing import List, Dict, override
from abc import ABC, abstractmethod

from src.enums.tipo_de_formatacao_enum import TipoFormatacao


class FormatadorDataFrame(ABC):


    def __init__(self, df: DataFrame):
        self.__df__ = df

    @property
    def df(self) -> DataFrame:
        return self.__df__
    @df.setter
    def df(self, df: DataFrame):
        self.__df__ = df

    @abstractmethod
    def formatar_cabecalho(self, df: DataFrame) -> DataFrame:
        pass
    @abstractmethod
    def formatar_dataframe(self, df: DataFrame) -> DataFrame:
        pass

    @classmethod
    def gera_formatador(cls, df: DataFrame, tipo: TipoFormatacao) -> FormatadorDataFrame:
        return FormatadorDataFrameInventario(df) if tipo == TipoFormatacao.INVENTARIO else FormatadorDataFrameCubo(df)



class FormatadorDataFrameInventario(FormatadorDataFrame):

        def __init__(self, df: DataFrame):
            super().__init__(df)
            self.primeira_linha = 7
            self.segunda_linha = 8
            self.corte_final = -1

        @override
        def formatar_dataframe(self, df: DataFrame):
            df = self.formatar_cabecalho(df)
            df = df.iloc[self.segunda_linha + 1:self.corte_final]
            return df

        @override
        def formatar_cabecalho(self, df: DataFrame) -> DataFrame:
            cabecalho: List[str] = []
            primeira_linha: pd.Series = df.iloc[self.primeira_linha]
            segunda_linha: pd.Series = df.iloc[self.segunda_linha]

            for i in range(len(df.columns)):

                if pd.notna(segunda_linha.iloc[i]):
                    cabecalho.append(str(segunda_linha.iloc[i]))
                else:
                    cabecalho.append(str(primeira_linha.iloc[i]))

            df.columns = cabecalho
            return df

class FormatadorDataFrameCubo(FormatadorDataFrame):

    def __init__(self, df: DataFrame):
        super().__init__(df)
        self.primeira_linha = 0
        self.corte_final = -5

    @override
    def formatar_dataframe(self, df: DataFrame):
        df = self.formatar_cabecalho(df)
        df = df.iloc[self.primeira_linha + 1 :self.corte_final]
        return df

    @override
    def formatar_cabecalho(self, df: DataFrame) -> DataFrame:
        cabecalho: List[str] = []
        cabecalho_invalido: pd.Index = df.columns
        primeira_linha: pd.Series = df.iloc[self.primeira_linha]

        for i in range(len(primeira_linha)):
            if pd.notna(primeira_linha.iloc[i]):
                cabecalho.append(str(primeira_linha.iloc[i]))
            else:
                cabecalho.append(str(cabecalho_invalido[i]))

        df.columns = cabecalho
        return df
