import pandas as pd
from pandas import DataFrame

from src.services.formatador_dataframe import FormatadorDataFrameFactory
from src.enums.tipo_de_formatacao_enum import TipoFormatacao

class Test_ValidaSPED:
    def test_valida_sped(self):
        df: DataFrame = pd.read_excel("tests/test_files/cubo.xlsx")
        formatador = FormatadorDataFrameFactory.criar_formatador(df=df, tipo=TipoFormatacao.SPED)
        df = formatador.formatar_dataframe(df)

        assert df["REG"].values == "H010"
        assert df["COD_ITEM"].values.__len__() <= 60
        assert df["UNID"].values.__len__() <= 6
        assert df["IND_PROP"].values == 0