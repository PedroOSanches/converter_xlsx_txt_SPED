class Company:

    def __init__(self, nome, apelido):
        self.apelido = apelido
        self.nome = nome

    @property
    def nome(self) -> str:
        return self.__nome__
    @nome.setter
    def nome(self, value: str):
        self.__nome__ = value
    @property
    def apelido(self) -> str:
        return self.__apelido__
    @apelido.setter
    def apelido(self, apelido: str):
        self.__apelido__ = apelido