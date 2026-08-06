import json
from pathlib import Path

from typing import Any


class CompanyRepository:

    def __init__(self):
        self.__caminho__ = Path(Path(__file__).parent.parent / "data" / "config.json")

    def __call__(self) -> dict[str, str]:
        return self.obter_compania()


    def obter_compania(self) -> dict[str, str]:
        with open(self.__caminho__, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            

        return dados["company"]