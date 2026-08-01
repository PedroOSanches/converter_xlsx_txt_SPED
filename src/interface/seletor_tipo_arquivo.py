import tkinter as tk
from tkinter.ttk import Combobox, Button
from enum import Enum
from src.enums.tipo_de_formatacao_enum import TipoFormatacao

class SeletorTipoArquivo:

    def seletor(self) -> TipoFormatacao:
        root = tk.Tk()
        root.title("Selecione o tipo de Relatório para ser formatado.")
        root.geometry("300x150")
        selecao = tk.StringVar()
        selecao.set(value=TipoFormatacao.CUBO.value)

        combo = Combobox(
            root,
            textvariable=selecao,
            values=[tipo.value for tipo in TipoFormatacao],
            state="readonly"
        )

        combo.pack(padx=20, pady=20)

        Button(
            root,
            text="Confirmar",
            command=root.destroy
        ).pack(pady=10)
        
        root.mainloop()
        return TipoFormatacao(selecao.get())