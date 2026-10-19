import customtkinter as ctk
from tkinter import filedialog

from converter import converter_ficheiro
from file_scanner import procurar_ficheiros


# =====================================
# FUNÇÕES
# =====================================

def escrever_log(texto):

    log.insert("end", texto + "\n")

    log.see("end")

    app.update()


def selecionar_ficheiro():

    ficheiro = filedialog.askopenfilename()

    if not ficheiro:
        return

    escrever_log(
        f"Ficheiro selecionado: {ficheiro}"
    )

    try:

        destino = converter_ficheiro(ficheiro)

        escrever_log(
            f"✓ Convertido: {destino}"
        )

    except Exception as erro:

        escrever_log(
            f"✗ Erro: {erro}"
        )


def selecionar_pasta():

    pasta = filedialog.askdirectory()

    if not pasta:
        return

    escrever_log(
        f"Pasta selecionada: {pasta}"
    )

    ficheiros = procurar_ficheiros(pasta)

    total = len(ficheiros)

    escrever_log(
        f"Encontrados {total} ficheiros."
    )

    if total == 0:

        escrever_log(
            "Nenhum ficheiro suportado encontrado."
        )

        return

    for indice, ficheiro in enumerate(ficheiros, start=1):
        
        percentagem = indice / total

        barra_progresso.set(percentagem)

        app.update()

        escrever_log(
            f"Ficheiro {indice} de {total}: {ficheiro.name}"
        )

        try:

            destino = converter_ficheiro(ficheiro)

            escrever_log(
                f"✓ Convertido para {destino.name}"
            )

        except Exception as erro:

            escrever_log(
                f"✗ Erro: {erro}"
            )

    escrever_log(
        "Conversão concluída."
    )


# =====================================
# INTERFACE
# =====================================

ctk.set_appearance_mode("dark")

ctk.set_default_color_theme("blue")

app = ctk.CTk()

app.title("Markdown Converter")

app.geometry("900x600")

# Título

titulo = ctk.CTkLabel(
    app,
    text="Conversor para Markdown",
    font=("Arial", 24, "bold")
)

titulo.pack(pady=20)

# Botão ficheiro

btn_ficheiro = ctk.CTkButton(
    app,
    text="Selecionar Ficheiro",
    command=selecionar_ficheiro
)

btn_ficheiro.pack(pady=10)

# Botão pasta

btn_pasta = ctk.CTkButton(
    app,
    text="Selecionar Pasta",
    command=selecionar_pasta
)

btn_pasta.pack(pady=10)

# Barra de progresso

barra_progresso = ctk.CTkProgressBar(app)

barra_progresso.pack(
    fill="x",
    padx=20,
    pady=10
)

barra_progresso.set(0)
# Área de log

log = ctk.CTkTextbox(
    app,
    width=800,
    height=350
)

log.pack(
    padx=20,
    pady=20,
    fill="both",
    expand=True
)

log.insert(
    "end",
    "Aplicação iniciada...\n"
)

app.mainloop()