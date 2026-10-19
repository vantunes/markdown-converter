import subprocess
import sys


DEPENDENCIAS = [
    "markitdown",
    "customtkinter",
    "tkinterdnd2"
]


def atualizar_dependencias(log_callback):

    log_callback("")
    log_callback("Verificação de atualizações iniciada...")

    for pacote in DEPENDENCIAS:

        try:

            log_callback(
                f"Atualizando {pacote}..."
            )

            resultado = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "pip",
                    "install",
                    "--upgrade",
                    pacote
                ],
                capture_output=True,
                text=True
            )

            if resultado.returncode == 0:

                log_callback(
                    f"[OK] {pacote} atualizado."
                )

            else:

                log_callback(
                    f" Erro ao atualizar {pacote}"
                )

                log_callback(
                    resultado.stderr
                )

        except Exception as erro:

            log_callback(
                f"[ERRO] Exceção em {pacote}: {erro}"
            )

    log_callback("")
    log_callback(
        "Atualização concluída."
    )

    log_callback(
        "Reinicie a aplicação."
    )