import subprocess
import sys


DEPENDENCIAS = [
    "markitdown",
    "customtkinter",
    "tkinterdnd2"
]


def atualizar_dependencias(escrever_log):

    escrever_log("")
    escrever_log("Verificação de atualizações iniciada...")

    for dependencia in DEPENDENCIAS:

        try:

            escrever_log(
                f"Atualizando {dependencia}..."
            )

            subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "pip",
                    "install",
                    "--upgrade",
                    dependencia
                ],
                check=True
            )

            escrever_log(
                f"✓ {dependencia} atualizado."
            )

        except Exception as erro:

            escrever_log(
                f"✗ Erro em {dependencia}: {erro}"
            )

    escrever_log("")
    escrever_log("Atualização concluída.")
    escrever_log("Reinicie a aplicação.")