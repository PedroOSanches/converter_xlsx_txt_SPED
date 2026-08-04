import pandas as pd
from pandas import DataFrame

from ..repositories.products_repository import ProductRepository



class EditorProdutos:

    products = ProductRepository()()

    def __init__(self) -> None:
        self.products: list[str] = ProductRepository()()

    def procura_produtos_dataframe(self, df: DataFrame):
        encontrados = df.loc[df["TXT_COMPL"].isin(self.products)] 
