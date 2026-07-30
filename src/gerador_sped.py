import pandas as pd

from pandas import DataFrame
from pathlib import Path

class GeradorSped:

    def gerar_csv_sped(self, nome: str, df: DataFrame, diretorio: Path):
        nome = nome.split('.')[0] + ".txt"

        path = diretorio / nome

        with open(path, "w", encoding="utf-8") as arquivo:
            for linha in df.itertuples(index=False, name=None):
                arquivo.write("|" + "|".join(map(str, linha)) + "|\n")