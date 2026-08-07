import re
from datetime import date

from ..domain.arquivo import Arquivo
from ..repositories.company_repository import CompanyRepository


class ArquivoService:

    def extrai_informacoes_nome(self, arquivo: Arquivo):
        print(arquivo.nome)
        self.descobre_data(arquivo=arquivo)
        print(arquivo.data)
        self.descobre_empresa(arquivo=arquivo)
        print(arquivo.empresa)

    def descobre_empresa(self, arquivo: Arquivo):   
        empresas = CompanyRepository()()

        nome_arquivo = arquivo.nome.lower()

        for empresa in empresas:
            apelido = empresa.apelido.lower()
            nome_empresa = empresa.nome.lower()

            if apelido in nome_arquivo or nome_empresa in nome_arquivo:
                arquivo.empresa = empresa
                return arquivo

        return arquivo

    def descobre_data(self, arquivo: Arquivo):
        match = re.search(r'(\d{2})[-/](\d{2})', arquivo.nome)
        if match:
            dia, mes = map(int, match.groups())
            try:
                arquivo.data = date(date.today().year, mes, dia)
            except ValueError:
                arquivo.data = None
