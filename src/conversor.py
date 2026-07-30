from pandas import DataFrame, read_excel
import os

from typing import List, Tuple, Dict, Literal
from pathlib import Path
from tkinter.filedialog import askdirectory

from src.interface.seletor_arquivos import SeletorArquivos
from src.leitor_excel import LeitorExcel
from src.gerador_sped import GeradorSped
from src.formatador_dataframe import FormatadorDataFrame
from src.exception.error_selecao import ErrorSelecao


class Conversor:

    @classmethod
    def converter(cls):
        seletor = SeletorArquivos()
        leitor = LeitorExcel()
        gerador = GeradorSped()
        formatador = FormatadorDataFrame()

        arquivos = seletor.selecionar_arquivos("Conversor XLSX - TXT Formato SPED: Selecione os arquivos desejados.")

        if arquivos is None:
            raise ErrorSelecao("Arquivos não selecionados:", "O programa será encerrado.")

        
        dataframes = leitor.obter_arquivos(arquivos=arquivos)

        diretorio_destino = seletor.selecionar_diretorio("Conversor XLSX - TXT Formato SPED: Selecione o diretório destino.")

        if diretorio_destino is None:
            raise ErrorSelecao("Diretório destino não selecionado:", "O programa será encerrado.")
        
        for df in dataframes:
            dataframes[df] = formatador.formatar_dataframe(dataframes[df])
            gerador.gerar_csv_sped(
                df,
                dataframes[df], 
                diretorio_destino
                )