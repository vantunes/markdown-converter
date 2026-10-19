import customtkinter as ctk
from tkinter import filedialog

from converter import converter_ficheiro
from file_scanner import procurar_ficheiros


# ==========================================
# FUNÇÕES
# ==========================================

def escrever_log(texto):

    log.insert("end", texto + "\n")

    log.see("end")

    app.update()


def mostrar_preview(ficheiro_md):

    try:

        with open(
            ficheiro_md,
            "r",
            encoding="utf-8"
        ) as f:

            conteudo = f.read()

        preview.delete("1.0", "end")

        preview.insert(
            "end",
            conteudo
        )

    except Exception as erro:

        escrever_log(
            f"Erro ao mostrar preview: {erro}"
        )


def selecionar_ficheiro():

    ficheiro = filedialog.askopenfilename()

    if not ficheiro:
        return

    try:

        barra_progresso.set(0)

        escrever_log(
            f"Ficheiro selecionado: {ficheiro}"
        )

        destino = converter_ficheiro(
            ficheiro
        )

        barra_progresso.set(1)

        escrever_log(
            f"✓ Convertido: {destino}"
        )

        mostrar_preview(destino)

    except Exception as erro:

        escrever_log(
            f"✗ Erro: {erro}"
        )


def selecionar_pasta():

    pasta = filedialog.askdirectory()

    if not pasta:
        return

    escrever_log("")
    escrever_log(
        f"Pasta selecionada: {pasta}"
    )

    ficheiros = procurar_ficheiros(
        pasta
    )

    total = len(ficheiros)

    escrever_log(
        f"Foram encontrados {total} ficheiros."
    )

    if total == 0:

        escrever_log(
            "Nenhum ficheiro suportado encontrado."
        )

        return

    barra_progresso.set(0)

    ultimo_md = None

    for indice, ficheiro in enumerate(
        ficheiros,
        start=1
    ):

        progresso = indice / total

        barra_progresso.set(
            progresso
        )

        app.update()

        escrever_log(
            f"Ficheiro {indice} de {total}: "
            f"{ficheiro.name}"
        )

        try:

            destino = converter_ficheiro(
                ficheiro
            )

            ultimo_md = destino

            escrever_log(
                f"✓ {destino.name}"
            )

        except Exception as erro:

            escrever_log(
                f"✗ Erro: {erro}"
            )

    escrever_log("")
    escrever_log(
        "Conversão concluída."
    )

    if ultimo_md:
        mostrar_preview(
            ultimo_md
        )


# ==========================================
# INTERFACE
# ==========================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()

app.title(
    "Markdown Converter"
)

app.geometry("1200x700")


# ==========================================
# TÍTULO
# ==========================================

titulo = ctk.CTkLabel(
    app,
    text="Conversor para Markdown",
    font=("Arial", 24, "bold")
)

titulo.pack(pady=20)


# ==========================================
# BOTÕES
# ==========================================

frame_botoes = ctk.CTkFrame(
    app
)

frame_botoes.pack(
    fill="x",
    padx=20,
    pady=10
)

btn_ficheiro = ctk.CTkButton(
    frame_botoes,
    text="Selecionar Ficheiro",
    command=selecionar_ficheiro
)

btn_ficheiro.pack(
    side="left",
    padx=10,
    pady=10
)

btn_pasta = ctk.CTkButton(
    frame_botoes,
    text="Selecionar Pasta",
    command=selecionar_pasta
)

btn_pasta.pack(
    side="left",
    padx=10,
    pady=10
)


# ==========================================
# PROGRESSO
# ==========================================

barra_progresso = ctk.CTkProgressBar(
    app
)

barra_progresso.pack(
    fill="x",
    padx=20,
    pady=10
)

barra_progresso.set(0)


# ==========================================
# ZONA INFERIOR
# ==========================================

frame_principal = ctk.CTkFrame(
    app
)

frame_principal.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=10
)


# ==========================================
# LOG
# ==========================================

frame_log = ctk.CTkFrame(
    frame_principal
)

frame_log.pack(
    side="left",
    fill="both",
    expand=True,
    padx=5
)

label_log = ctk.CTkLabel(
    frame_log,
    text="LOG"
)

label_log.pack(
    pady=5
)

log = ctk.CTkTextbox(
    frame_log
)

log.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)


# ==========================================
# PREVIEW MARKDOWN
# ==========================================

frame_preview = ctk.CTkFrame(
    frame_principal
)

frame_preview.pack(
    side="left",
    fill="both",
    expand=True,
    padx=5
)

label_preview = ctk.CTkLabel(
    frame_preview,
    text="PREVIEW MARKDOWN"
)

label_preview.pack(
    pady=5
)

preview = ctk.CTkTextbox(
    frame_preview
)

preview.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)


# ==========================================
# INÍCIO
# ==========================================

log.insert(
    "end",
    "Aplicação iniciada...\n"
)

app.mainloop()