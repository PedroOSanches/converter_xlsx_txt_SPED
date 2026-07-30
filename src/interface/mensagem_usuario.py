from tkinter.messagebox import showinfo


class Mensagem():
    @classmethod
    def informacao(cls, title: str, msg: str):
        showinfo(
            title=title,
            message=msg,
            icon='info'
            )