from pathlib import Path

from settings import EXTENSOES_SUPORTADAS


def procurar_ficheiros(pasta):

    encontrados = []

    for ficheiro in Path(pasta).rglob("*"):

        if ficheiro.is_file():

            if ficheiro.suffix.lower() in EXTENSOES_SUPORTADAS:

                encontrados.append(ficheiro)

    return encontrados