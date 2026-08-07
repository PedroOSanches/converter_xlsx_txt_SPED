from enum import Enum
from dataclasses import dataclass
from collections.abc import Callable
from pandas import DataFrame

@dataclass
class ConfigFormatacoes:
    nome: str
    coluna_chave: str | None = None
    colunas_soma: set[str] | None = None
    colunas_recalcular: dict[str, Callable[[DataFrame], DataFrame]] | None = None
    ordem_colunas: list[str] | None = None


class TipoFormatacao(Enum):

    CUBO = ConfigFormatacoes(
        nome="Cubo"
    )

    INVENTARIO = ConfigFormatacoes(
        nome="Livro Inventário"
    )

    SPED = ConfigFormatacoes(
        nome="SPED",
        coluna_chave="COD_ITEM",
        colunas_soma={"QTD"},
        colunas_recalcular={
            "VL_ITEM": lambda df: df.assign(
                VL_ITEM=df["QTD"] * df["VL_UNIT"]
            )
        },
        ordem_colunas=[
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
    )