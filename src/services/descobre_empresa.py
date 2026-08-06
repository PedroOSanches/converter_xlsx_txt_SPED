from ..repositories.company_repository import CompanyRepository
from pandas import DataFrame

class CompanyService:

    def __init__(self):
        self.__company_repository__ = CompanyRepository()

    def descobre_empresa(self, dataframes: dict[str, DataFrame]) -> dict[str, list[DataFrame]]:
        empresas = self.__company_repository__()

        dataframe_por_empresa: dict[str, list[DataFrame]] = {}

        for nome_arquivo, df in dataframes.items():
            nome_arquivo = nome_arquivo.lower()

            for apelido, empresa in empresas.items():
                if (
                    apelido.lower() in nome_arquivo 
                    or empresa.lower() in nome_arquivo
                    ):
                    dataframe_por_empresa.setdefault(empresa, []).append(df)
                    break

        return dataframe_por_empresa