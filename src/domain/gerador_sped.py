import pandas as pd
from pandas import DataFrame
from pathlib import Path
from src.enums.tipo_de_formatacao_enum import TipoFormatacao


class GeradorSped:

    def gerar_csv_sped(self, nome: str, df: DataFrame, diretorio: Path, type: TipoFormatacao):
        nome = nome.split('.')[0] + ".txt"

        path = diretorio / nome


        if type == TipoFormatacao.CUBO:
            with open(path, "w", encoding="utf-8") as arquivo:
                for linha in df.itertuples(index=False, name=None):
                    arquivo.write("|" + "|".join(map(str, linha)) + "|\n")
        else:
            with open(path, "w", encoding="utf-8") as arquivo:
                arquivo.write("|" + "|".join(map(str, df.columns)) + "\n")

                for linha in df.itertuples(index=False, name=None):
                    arquivo.write("|" + "|".join(map(str, linha)) + "|\n")