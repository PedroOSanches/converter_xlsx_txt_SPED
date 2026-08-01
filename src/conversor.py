from pandas import DataFrame, read_excel
import os

from typing import List, Tuple, Dict, Literal
from pathlib import Path
from tkinter.filedialog import askdirectory

from src.interface.seletor_arquivos import SeletorArquivos
from src.interface.seletor_tipo_arquivo import SeletorTipoArquivo
from src.domain.leitor_excel import LeitorExcel
from src.domain.gerador_sped import GeradorSped
from src.domain.formatador_dataframe import FormatadorDataFrame
from src.exception.error_selecao import ErrorSelecao


class Conversor:

    @classmethod
    def converter(cls):

        seletor_arquivo = SeletorArquivos()
        seletor_tipo = SeletorTipoArquivo()
        leitor = LeitorExcel()
        gerador = GeradorSped()
        arquivos = seletor_arquivo.selecionar_arquivos("Conversor XLSX - TXT Formato SPED: Selecione os arquivos desejados.")

        if arquivos is None:
            raise ErrorSelecao("Arquivos não selecionados:", "O programa será encerrado.")

        tipo = seletor_tipo.seletor()
        dataframes = leitor.obter_dataframes(arquivos=arquivos)

        diretorio_destino = seletor_arquivo.selecionar_diretorio("Conversor XLSX - TXT Formato SPED: Selecione o diretório destino.")

        if diretorio_destino is None:
            raise ErrorSelecao("Diretório destino não selecionado:", "O programa será encerrado.")
        
        for df in dataframes:
            formatador = FormatadorDataFrame.gera_formatador(dataframes[df], tipo)
            dataframes[df] = formatador.formatar_dataframe(dataframes[df])
            gerador.gerar_csv_sped(
                df,
                dataframes[df], 
                diretorio_destino,
                tipo
                )