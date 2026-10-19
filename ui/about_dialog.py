import platform
import importlib.metadata

from tkinter import messagebox

from settings import (
    APP_NOME,
    APP_VERSAO,
    APP_AUTOR
)


class AboutDialog:

    @staticmethod
    def show():

        try:
            versao_markitdown = (
                importlib.metadata.version(
                    "markitdown"
                )
            )
        except Exception:
            versao_markitdown = "Não disponível"

        try:
            versao_customtkinter = (
                importlib.metadata.version(
                    "customtkinter"
                )
            )
        except Exception:
            versao_customtkinter = "Não disponível"

        try:
            versao_tkinterdnd2 = (
                importlib.metadata.version(
                    "tkinterdnd2"
                )
            )
        except Exception:
            versao_tkinterdnd2 = "Não disponível"

        mensagem = f"""
{APP_NOME}

Versão: {APP_VERSAO}

Autor: {APP_AUTOR}

Python: {platform.python_version()}

Bibliotecas:

MarkItDown: {versao_markitdown}

CustomTkinter: {versao_customtkinter}

TkinterDnD2: {versao_tkinterdnd2}
"""

        messagebox.showinfo(
            "Sobre",
            mensagem
        )