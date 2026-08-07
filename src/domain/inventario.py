import uuid
from datetime import date
from pandas import DataFrame
from typing import Optional
from .arquivo import Arquivo
from .company import Company

class Inventario:

    def __init__(
            self, 
            empresa: Company, 
            inventario: DataFrame, 
            data: date, 
            motivo: str = "01",
            ):
        self.empresa = empresa
        self.data = data
        self.motivo = motivo
        self.inventario = inventario

    @property
    def empresa(self) -> Company:
        return self.__empresa__

    @empresa.setter
    def empresa(self, empresa: Company):
        self.__empresa__ = empresa

    @property
    def data(self) -> date:
        return self.__data__

    @data.setter
    def data(self, data: date):
        self.__data__ = data

    @property
    def motivo(self) -> str:
        return self.__motivo__

    @motivo.setter
    def motivo(self, motivo: str):
        self.__motivo__ = motivo

    @property
    def inventario(self) -> DataFrame:
        return self.__inventario__

    @inventario.setter
    def inventario(self, inventario: DataFrame):
        self.__inventario__ = inventario
