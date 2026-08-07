from pandas import DataFrame
from datetime import date
from typing import Optional

from .company import Company

class Arquivo:

    def __init__(
            self,
            nome: str,
            df: DataFrame,
            empresa: Optional[Company] = None,
            data: Optional[date] = None
            ) -> None:
        self.nome = nome
        self.df = df
        self.empresa = empresa
        self.data = data