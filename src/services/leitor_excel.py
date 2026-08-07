import pandas as pd
from pandas import DataFrame
from typing import Tuple, Literal, Dict
from ..domain.arquivo import Arquivo
from .arquivo_service import ArquivoService
class LeitorExcel:

    def obter_arquivos(self, arquivos_recebidos: Tuple[str, ...] | Literal['']) -> list[Arquivo]:
        arquivo_service = ArquivoService()
        arquivos: list[Arquivo] = []
        for arquivo in arquivos_recebidos:
            nome_arquivo = arquivo.split("/")[-1]
            dataframe = pd.read_excel(arquivo)
            arquivo = Arquivo(nome_arquivo, dataframe)
            arquivo_service.extrai_informacoes_nome(arquivo=arquivo)
            arquivos.append(arquivo)
        return arquivos