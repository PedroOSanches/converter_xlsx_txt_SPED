import json
from pathlib import Path
from typing import Any


class ProductRepository:

    
    def __init__(self) -> None:
        self.__caminho__ = (Path(__file__).parent.parent / "data" / "products.json" )

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return self.obter_produtos


    def obter_produtos(self) -> list[str]:
        with open(self.__caminho__, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        return dados["products"]