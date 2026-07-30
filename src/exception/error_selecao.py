class ErrorSelecao(Exception):
    def __init__(self, title: str, msg: str) -> None:
        self.message = msg
        self.title = title
        super().__init__(msg)


    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self, title: str):
        self.__title = title
    @property
    def message(self):
        return self.__message
    @message.setter
    def message(self, msg: str) -> None:
        self.__message = msg