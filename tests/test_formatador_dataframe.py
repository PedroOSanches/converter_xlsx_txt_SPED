import pandas as pd
from pandas import DataFrame
from src.enums.tipo_de_formatacao_enum import TipoFormatacao
from src.services.formatador_dataframe import FormatadorDataFrameFactory

class Test_FormatadorDataFrame:

    def test_formatador_cabecalho_inventario(self):
        df: DataFrame = pd.read_excel('tests/test_files/inventario.xlsx')
        formatador = FormatadorDataFrameFactory.criar_formatador(df=df, tipo=TipoFormatacao.INVENTARIO)
        df = formatador.formatar_cabecalho(df)
        cabecalho = df.columns.tolist()
        print(cabecalho)


        assert cabecalho == ['NCM', 'Código', 'Discriminação', 'UN', 'Quant.', 'Unitário', 'Total', 'ICMS Recuperavel', 'Total S/ ICMS P/ fins de I.R.']

    def test_formatar_dataframe_inventario(self):
        df: DataFrame = pd.read_excel('tests/test_files/inventario.xlsx')
        formatador = FormatadorDataFrameFactory.criar_formatador(df=df, tipo=TipoFormatacao.INVENTARIO)
        df = formatador.formatar_dataframe(df)
        df_primeira_linha = df.iloc[0].tolist()
        df_ultima_linha = df.iloc[-1].tolist()

        linha_teste = [32064990, 7898706130038, 'PO XADREZ MARROM   500GR', 'CX', 14, 17.48004, 244.72055999999998]

        assert df_primeira_linha == linha_teste
        assert df_ultima_linha == linha_teste

    def test_formatador_cabecalho_cubo(self):
        df: DataFrame = pd.read_excel('tests/test_files/cubo.xlsx')
        formatador = FormatadorDataFrameFactory.criar_formatador(df=df, tipo=TipoFormatacao.CUBO)
        print(df)
        df = formatador.formatar_cabecalho(df)
        cabecalho = df.columns.tolist()

        assert cabecalho == ['CODIGO', 'Codigo de Barras', 'DESCRICAO', 'TUNIDADE', 'CST', 'ICMS', 'QTDESTOQUE', 'NPRECOCUSTO', 'NPRECOCUSTOTOTAL', 'VALORICMS']

    def test_formatar_dataframe_cubo(self):
        df: DataFrame = pd.read_excel('tests/test_files/cubo.xlsx')
        formatador = FormatadorDataFrameFactory.criar_formatador(df=df, tipo=TipoFormatacao.CUBO)
        df = formatador.formatar_dataframe(df)
        df_primeira_linha = df.iloc[0].tolist()
        df_ultima_linha = df.iloc[-1].tolist()
        linha_teste = [4, '7898706130038', 'PO XADREZ MARROM   500GR', 'CX', '060', 18, 7, 17.48, 122.36, 'R$ 0,00']
        assert df_primeira_linha == linha_teste
        assert df_ultima_linha == linha_teste

    def test_formatar_dataframe_sped(self):
        df: DataFrame = pd.read_excel("tests/test_files/cubo.xlsx")
        formatador = FormatadorDataFrameFactory.criar_formatador(df=df, tipo=TipoFormatacao.SPED)
        df = formatador.formatar_dataframe(df)

        assert df.columns.to_list() == ["REG", "COD_ITEM", "UNID", "QTD", "VL_UNIT", "VL_ITEM", "IND_PROP", "TXT_COMPL", "VL_ITEM_IR"]
        assert df.iloc[0].to_list() == ['H010', 4, 'CX', 7, 17.48, 122.36, 0, 'PO XADREZ MARROM   500GR', 122.36]
        assert df.iloc[-1].to_list() == ['H010', 4, 'CX', 7, 17.48, 122.36, 0, 'PO XADREZ MARROM   500GR', 122.36]