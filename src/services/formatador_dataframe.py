import pandas as pd
from pandas import DataFrame
from typing import List, Dict, override
from abc import ABC, abstractmethod
from datetime import date
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
    def formatar_dataframe(self) -> DataFrame:
        pass
    @classmethod
    def reordena_dataframe(cls, df: DataFrame, ordem_colunas: list[str]):
        return df[ordem_colunas] 


class FormatadorDataFrameFactory:

    @staticmethod
    def criar_formatador(tipo: TipoFormatacao, df: DataFrame) -> FormatadorDataFrame:
        if tipo == TipoFormatacao.INVENTARIO:
            return FormatadorDataFrameInventario(df)
        elif tipo == TipoFormatacao.CUBO:
            return FormatadorDataFrameCubo(df)
        elif tipo == TipoFormatacao.SPED:
            return FormatadorDataFrameSPED(df)
        else:
            raise ValueError(f"Tipo de formatação inválido: {tipo}")



class FormatadorDataFrameInventario(FormatadorDataFrame):

        def __init__(self, df: DataFrame):
            super().__init__(df)
            self.primeira_linha = 6
            self.segunda_linha = 7
            self.corte_final = -1
            self.colunas_indesejadas = ["ICMS Recuperavel", "Total S/ ICMS P/ fins de I.R."]

        @override
        def formatar_dataframe(self):
            df = self.df
            print("Formatando DataFrame do tipo INVENTARIO...\n", df)
            df = self.formatar_cabecalho(df)
            df = df.iloc[self.segunda_linha + 1 :self.corte_final]
            df = df.drop(columns=self.colunas_indesejadas, errors='ignore')
            print("DataFrame formatado com sucesso.\n", df.iloc[0].to_list())
            return df

        @override
        def formatar_cabecalho(self, df: DataFrame) -> DataFrame:
            cabecalho: List[str] = []
            primeira_linha: pd.Series = df.iloc[self.primeira_linha]
            print(f"Primeira linha: Index{primeira_linha.name}\n", primeira_linha)
            segunda_linha: pd.Series = df.iloc[self.segunda_linha]
            print(f"Segunda linha: Index{segunda_linha.name}\n", segunda_linha)

            for i in range(len(df.columns)):

                if pd.notna(segunda_linha.iloc[i]):
                    cabecalho.append(str(segunda_linha.iloc[i]))
                else:
                    cabecalho.append(str(primeira_linha.iloc[i]))

            df.columns = cabecalho
            print("Cabeçalho formatado com sucesso.\n", df)
            return df

class FormatadorDataFrameCubo(FormatadorDataFrame):

    def __init__(self, df: DataFrame):
        super().__init__(df)
        self.primeira_linha = 0
        self.corte_final = -5

    @override
    def formatar_dataframe(self):
        df = self.df
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



class FormatadorDataFrameSPED(FormatadorDataFrameCubo):
    def __init__(self, df: DataFrame):
        super().__init__(df)


    @override
    def formatar_dataframe(self) -> DataFrame:
        df = super().formatar_dataframe()

        new_df = df.copy()
        new_df.insert(0, "REG", "H010")


        new_df = new_df.rename(columns={
            'CODIGO': "COD_ITEM", 
            'TUNIDADE': "UNID",
            'QTDESTOQUE': "QTD",
            'NPRECOCUSTO': "VL_UNIT",
            'NPRECOCUSTOTOTAL': "VL_ITEM",
            'DESCRICAO': "TXT_COMPL"
            })

        new_df["IND_PROP"] = 0
        new_df["QTD"] = new_df["QTD"].round(3)
        new_df["VL_UNIT"] = new_df["VL_UNIT"].round(6)
        new_df["VL_ITEM"] = new_df["VL_ITEM"].round(2)
        new_df["VL_ITEM_IR"] = new_df["VL_ITEM"].round(2)

        new_df = new_df.drop(
            columns=[
                'CST', 
                'ICMS', 
                'VALORICMS', 
                'Codigo de Barras'
                ]
            )
        new_df = new_df[
        [
            "REG",
            "COD_ITEM",
            "UNID",
            "QTD",
            "VL_UNIT",
            "VL_ITEM",
            "IND_PROP",
            "TXT_COMPL",
            "VL_ITEM_IR"
        ]
    ]
        return new_df