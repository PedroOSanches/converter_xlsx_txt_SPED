from src.conversor import Conversor

from src.interface.mensagem_usuario import Mensagem
from src.exception.error_selecao import ErrorSelecao

try:
    Conversor.converter()
except ErrorSelecao as err:
    Mensagem.informacao(err.title, err.message)