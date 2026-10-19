from pathlib import Path

from markitdown import MarkItDown


md = MarkItDown()


def converter_ficheiro(caminho):

    caminho = Path(caminho)

    resultado = md.convert(str(caminho))

    destino = caminho.with_suffix(".md")

    with open(
        destino,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(
            resultado.text_content
        )

    return destino