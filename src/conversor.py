from .interface.seletor_arquivos import SeletorArquivos
from .interface.seletor_tipo_arquivo import SeletorTipoArquivo
from .services.leitor_excel import LeitorExcel
from .services.gerador_sped import GeradorSped
from .services.formatador_dataframe import FormatadorDataFrameFactory
from .services.company_service import CompanyService
from .services.concatenador_dataframes import ConcatenadorDataFrames
from .services.gera_bloco_h005 import adiciona_h005
from .services.inventario_service import InventarioService
from .exception.error_selecao import ErrorSelecao

class Conversor:

    @classmethod
    def converter(cls):

        seletor_arquivo = SeletorArquivos()
        seletor_tipo = SeletorTipoArquivo()
        leitor = LeitorExcel()
        formatador = FormatadorDataFrameFactory()
        gerador = GeradorSped()
        concatenador = ConcatenadorDataFrames()
        inventario_service = InventarioService(concatenador)
        arquivos = seletor_arquivo.selecionar_arquivos("Conversor XLSX - TXT Formato SPED: Selecione os arquivos desejados.")

        if arquivos is None:
            raise ErrorSelecao("Arquivos não selecionados:", "O programa será encerrado.")

        tipo = seletor_tipo.seletor()

        arquivos = leitor.obter_arquivos(arquivos_recebidos=arquivos)


        diretorio_destino = seletor_arquivo.selecionar_diretorio("Conversor XLSX - TXT Formato SPED: Selecione o diretório destino.")

        if diretorio_destino is None:
            raise ErrorSelecao("Diretório destino não selecionado:", "O programa será encerrado.")

        for i, a in enumerate(arquivos):
            formatador_utilizado = formatador.criar_formatador(tipo, a.df)
            arquivos[i].df = formatador_utilizado.formatar_dataframe()

        inventarios = inventario_service.criar_inventarios(arquivos=arquivos, tipo=tipo)

        for i in inventarios:
            i.inventario = adiciona_h005(i.inventario, "VL_ITEM", i.data)
            print(i.inventario)
            gerador.gerar(f"inventario_{i.empresa.nome}_{i.data}", df=i.inventario, diretorio=diretorio_destino, type=tipo)