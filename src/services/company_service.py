from ..repositories.company_repository import CompanyRepository
from pandas import DataFrame
from ..domain.arquivo import Arquivo


class CompanyService:

    def __init__(self):
        self.__company_repository__ = CompanyRepository()

    def descobre_empresa(self, arquivos: list[Arquivo]) -> dict[str, list[DataFrame]]:
        empresas = self.__company_repository__()

        dataframe_por_empresa: dict[str, list[DataFrame]] = {}

        for arquivo in arquivos:
            nome_arquivo = arquivo.nome.lower()
            df = arquivo.df
            for empresa in empresas:
                if (
                    empresa.apelido.lower() in nome_arquivo 
                    or empresa.nome.lower() in nome_arquivo
                    ):
                    dataframe_por_empresa.setdefault(empresa.nome, []).append(df)
                    print(df.attrs['nome_arquivo'])
                    break

        return dataframe_por_empresa