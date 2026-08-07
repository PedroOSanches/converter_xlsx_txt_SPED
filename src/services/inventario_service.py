from ..domain.inventario import Inventario
from ..domain.arquivo import Arquivo
from collections import defaultdict

from ..services.concatenador_dataframes import ConcatenadorDataFrames
from ..enums.tipo_de_formatacao_enum import TipoFormatacao


class InventarioService:

    def __init__(
        self,
        concatenador: ConcatenadorDataFrames
    ):
        self.concatenador = concatenador


    def criar_inventarios(
        self,
        arquivos: list[Arquivo],
        tipo: TipoFormatacao
    ) -> list[Inventario]:

        grupos = defaultdict(list)

        for arquivo in arquivos:
            chave = (arquivo.empresa, arquivo.data)
            grupos[chave].append(arquivo)

        inventarios = []
        arquivos_grupo: list[Arquivo]
        for (empresa, data), arquivos_grupo in grupos.items():

            dataframes = [
                arquivo.df
                for arquivo in arquivos_grupo
            ]

            dataframe_inventario = self.concatenador.concatena_dataframes(
                dataframes,
                tipo.value
            )

            inventario = Inventario(
                empresa=empresa,
                data=data,
                inventario=dataframe_inventario
            )

            inventarios.append(inventario)

        return inventarios