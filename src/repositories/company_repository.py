import json
from pathlib import Path

from typing import Any
from ..domain.company import Company

class CompanyRepository:

    def __init__(self):
        self.__caminho__ = Path(Path(__file__).parent.parent / "data" / "config.json")
        self.__empresas__: list[Company] = []
        self.create_company(self.obter_compania())

    def __call__(self) -> list[Company]:
        return self.get_empresas()


    def obter_compania(self) -> dict[str, str]:
        with open(self.__caminho__, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            

        return dados["company"]

    def create_company(self, empresas: dict[str, str]):
        for apelido, empresa in empresas.items():
            self.__empresas__.append(Company(apelido=apelido, nome=empresa))

    def get_empresas(self) -> list[Company]:
        return self.__empresas__