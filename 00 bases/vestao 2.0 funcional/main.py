import platform
import importlib.metadata
from tkinter import messagebox

import customtkinter as ctk

from tkinter import filedialog

import threading
import time

from converter import converter_ficheiro
from file_scanner import procurar_ficheiros

from updater import atualizar_dependencias

from settings import (
    APP_NOME,
    APP_VERSAO,
    APP_AUTOR,
    APP_TEMA,
    APP_COR,
    LARGURA_JANELA,
    ALTURA_JANELA
)


# ==========================================
# VARIÁVEIS GLOBAIS
# ==========================================

cronometro_ativo = False
inicio_tempo = 0


# ==========================================
# CRONÓMETRO
# ==========================================

def atualizar_cronometro():

    if cronometro_ativo:

        tempo = int(
            time.time() - inicio_tempo
        )

        horas = tempo // 3600

        minutos = (
            tempo % 3600
        ) // 60

        segundos = tempo % 60

        label_tempo.configure(
            text=(
                f"Tempo: "
                f"{horas:02}:"
                f"{minutos:02}:"
                f"{segundos:02}"
            )
        )

        app.after(
            1000,
            atualizar_cronometro
        )


# ==========================================
# LOG
# ==========================================

def escrever_log(texto):

    log.insert(
        "end",
        texto + "\n"
    )

    log.see("end")


# ==========================================
# PREVIEW
# ==========================================

def mostrar_preview(ficheiro_md):

    try:

        with open(
            ficheiro_md,
            "r",
            encoding="utf-8"
        ) as f:

            conteudo = f.read()

        preview.delete(
            "1.0",
            "end"
        )

        preview.insert(
            "end",
            conteudo
        )

    except Exception as erro:

        escrever_log(
            f"Erro preview: {erro}"
        )


# ==========================================
# ATUALIZAÇÕES
# ==========================================

def atualizar_programa():

    threading.Thread(
        target=lambda: atualizar_dependencias(
            escrever_log
        ),
        daemon=True
    ).start()


# ==========================================
# FICHEIRO
# ==========================================

def selecionar_ficheiro():

    ficheiro = filedialog.askopenfilename()

    if not ficheiro:
        return

    threading.Thread(
        target=converter_ficheiro_thread,
        args=(ficheiro,),
        daemon=True
    ).start()


def converter_ficheiro_thread(ficheiro):

    global cronometro_ativo
    global inicio_tempo

    try:

        barra_progresso.set(0)

        escrever_log("")
        escrever_log(
            f"Conversão iniciada:"
        )
        escrever_log(
            ficheiro
        )

        inicio_tempo = time.time()

        cronometro_ativo = True

        atualizar_cronometro()

        destino = converter_ficheiro(
            ficheiro
        )

        cronometro_ativo = False

        tempo_total = (
            time.time()
            - inicio_tempo
        )

        barra_progresso.set(1)

        escrever_log(
            f"✓ Convertido: {destino}"
        )

        escrever_log(
            f"Tempo total: "
            f"{tempo_total:.1f} s"
        )

        mostrar_preview(destino)

    except Exception as erro:

        cronometro_ativo = False

        escrever_log(
            f"✗ Erro: {erro}"
        )


# ==========================================
# PASTA
# ==========================================

def selecionar_pasta():

    pasta = filedialog.askdirectory()

    if not pasta:
        return

    threading.Thread(
        target=converter_pasta_thread,
        args=(pasta,),
        daemon=True
    ).start()


def converter_pasta_thread(pasta):

    global cronometro_ativo
    global inicio_tempo

    ficheiros = procurar_ficheiros(
        pasta
    )

    total = len(ficheiros)

    escrever_log("")
    escrever_log(
        f"Pasta: {pasta}"
    )

    escrever_log(
        f"Encontrados "
        f"{total} ficheiros."
    )

    if total == 0:
        return

    inicio_tempo = time.time()

    cronometro_ativo = True

    atualizar_cronometro()

    ultimo_md = None

    for indice, ficheiro in enumerate(
        ficheiros,
        start=1
    ):

        inicio_ficheiro = time.time()

        barra_progresso.set(
            indice / total
        )

        escrever_log("")
        escrever_log(
            f"Ficheiro "
            f"{indice} de {total}"
        )

        escrever_log(
            ficheiro.name
        )

        try:

            destino = converter_ficheiro(
                ficheiro
            )

            ultimo_md = destino

            tempo_ficheiro = (
                time.time()
                - inicio_ficheiro
            )

            escrever_log(
                f"✓ {destino.name}"
            )

            escrever_log(
                f"Tempo ficheiro: "
                f"{tempo_ficheiro:.1f}s"
            )

        except Exception as erro:

            escrever_log(
                f"✗ Erro: {erro}"
            )

    cronometro_ativo = False

    tempo_total = (
        time.time()
        - inicio_tempo
    )

    escrever_log("")
    escrever_log(
        "Conversão concluída."
    )

    escrever_log(
        f"Tempo total pasta: "
        f"{tempo_total:.1f}s"
    )

    if ultimo_md:

        mostrar_preview(
            ultimo_md
        )

# ==================================================
# SOBRE
# ==================================================

def mostrar_sobre():

    try:
        versao_markitdown = importlib.metadata.version(
            "markitdown"
        )
    except:
        versao_markitdown = "Não disponível"

    try:
        versao_customtkinter = importlib.metadata.version(
            "customtkinter"
        )
    except:
        versao_customtkinter = "Não disponível"

    try:
        versao_tkinterdnd2 = importlib.metadata.version(
            "tkinterdnd2"
        )
    except:
        versao_tkinterdnd2 = "Não disponível"

    mensagem = (
        f"{APP_NOME}\n"
        f"Versão: {APP_VERSAO}\n\n"
        f"Python: {platform.python_version()}\n"
        f"MarkItDown: {versao_markitdown}\n"
        f"CustomTkinter: {versao_customtkinter}\n"
        f"TkinterDnD2: {versao_tkinterdnd2}\n\n"
        f"Autor: {APP_AUTOR}"
    )

    messagebox.showinfo(
        "Sobre",
        mensagem
    )
# ==========================================
# INTERFACE
# ==========================================

ctk.set_appearance_mode(
    APP_TEMA
)

ctk.set_default_color_theme(
    APP_COR
)

app = ctk.CTk()

menu_bar = ctk.CTkFrame(
    app,
    height=40
)

menu_bar.pack(
    fill="x",
    padx=10,
    pady=5
)
btn_sobre = ctk.CTkButton(
    menu_bar,
    text="Sobre",
    width=100,
    command=mostrar_sobre
)

btn_sobre.pack(
    side="right",
    padx=5,
    pady=5
)

app.title(
    f"{APP_NOME} v{APP_VERSAO}"
)

app.geometry(
    f"{LARGURA_JANELA}x{ALTURA_JANELA}"
)


titulo = ctk.CTkLabel(
    app,
    text=f"{APP_NOME} v{APP_VERSAO}",
    font=("Arial", 24, "bold")
)

titulo.pack(pady=15)


frame_botoes = ctk.CTkFrame(app)

frame_botoes.pack(
    fill="x",
    padx=20,
    pady=10
)


ctk.CTkButton(
    frame_botoes,
    text="Selecionar Ficheiro",
    command=selecionar_ficheiro
).pack(
    side="left",
    padx=5,
    pady=10
)


ctk.CTkButton(
    frame_botoes,
    text="Selecionar Pasta",
    command=selecionar_pasta
).pack(
    side="left",
    padx=5,
    pady=10
)


ctk.CTkButton(
    frame_botoes,
    text="Atualizar Dependências",
    command=atualizar_programa
).pack(
    side="left",
    padx=5,
    pady=10
)


barra_progresso = ctk.CTkProgressBar(
    app
)

barra_progresso.pack(
    fill="x",
    padx=20,
    pady=10
)

barra_progresso.set(0)


label_tempo = ctk.CTkLabel(
    app,
    text="Tempo: 00:00:00"
)

label_tempo.pack()


frame_principal = ctk.CTkFrame(
    app
)

frame_principal.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=10
)


log = ctk.CTkTextbox(
    frame_principal
)

log.pack(
    side="left",
    fill="both",
    expand=True,
    padx=5,
    pady=5
)


preview = ctk.CTkTextbox(
    frame_principal
)

preview.pack(
    side="left",
    fill="both",
    expand=True,
    padx=5,
    pady=5
)


log.insert(
    "end",
    f"{APP_NOME} v{APP_VERSAO} iniciado.\n"
)

app.mainloop()