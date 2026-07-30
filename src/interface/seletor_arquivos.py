import tkinter as tk
from tkinter.filedialog import askdirectory, askopenfilenames

from pathlib import Path
from typing import Tuple, Literal, List

class SeletorArquivos:

    def selecionar_arquivos(
            self,
            title: str,
            filetypes: List[Tuple[str, str]] = [("Planilhas Excel", "*.xlsx")]
            ) -> Tuple[str, ...] | Literal[''] | None:

        arquivos =  askopenfilenames(
            title=title, 
            filetypes=filetypes
            )

        if not arquivos:
            return None

        return arquivos

    def selecionar_diretorio(self, title: str) -> Path | None:
        diretorio = askdirectory(
            title=title
        )

        if not diretorio:
            return None
        
        return Path(diretorio) 