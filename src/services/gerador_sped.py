import pandas as pd
from pandas import DataFrame
from pathlib import Path
from src.enums.tipo_de_formatacao_enum import TipoFormatacao


class GeradorSped:

    def gerar(
    self,
    nome: str,
    df: DataFrame,
    diretorio: Path,
    type: TipoFormatacao
    ):
        nome_base = Path(nome).stem

        path_xlsx = diretorio / f"{nome_base}.xlsx"
        path_txt = diretorio / f"{nome_base}.txt"

        with open(path_txt, "w", encoding="utf-8") as arquivo:

            if type == TipoFormatacao.INVENTARIO:
                arquivo.write(
                    "|" + "|".join(map(str, df.columns)) + "|\n"
                )

            for linha in df.itertuples(index=False, name=None):
                arquivo.write("|" + "|".join("" if pd.isna(valor) else str(valor) for valor in linha) + "|\n")

        if type == TipoFormatacao.INVENTARIO:
            df.to_excel(
                path_xlsx,
                index=False,
                engine="openpyxl",
                sheet_name="SPED",
                header=True
            )