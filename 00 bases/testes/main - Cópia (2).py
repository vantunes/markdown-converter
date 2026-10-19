import customtkinter as ctk
from tkinter import filedialog
import threading
import time

from converter import converter_ficheiro
from file_scanner import procurar_ficheiros


# ==================================================
# VARIÁVEIS GLOBAIS
# ==================================================

cronometro_ativo = False
inicio_tempo = 0


# ==================================================
# CRONÓMETRO
# ==================================================

def atualizar_cronometro():

    if cronometro_ativo:

        tempo = int(time.time() - inicio_tempo)

        horas = tempo // 3600
        minutos = (tempo % 3600) // 60
        segundos = tempo % 60

        label_tempo.configure(
            text=f"Tempo decorrido: {horas:02}:{minutos:02}:{segundos:02}"
        )

        app.after(
            1000,
            atualizar_cronometro
        )


# ==================================================
# LOG
# ==================================================

def escrever_log(texto):

    log.insert(
        "end",
        texto + "\n"
    )

    log.see("end")


# ==================================================
# PREVIEW
# ==================================================

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


# ==================================================
# FICHEIRO ÚNICO
# ==================================================

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

        escrever_log("")
        escrever_log("Conversão iniciada")
        escrever_log(ficheiro)

        barra_progresso.set(0)

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
            f"Tempo total: {tempo_total:.1f} segundos"
        )

        mostrar_preview(
            destino
        )

    except Exception as erro:

        cronometro_ativo = False

        escrever_log(
            f"✗ Erro: {erro}"
        )


# ==================================================
# PASTA
# ==================================================

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

    escrever_log("")
    escrever_log(
        f"Pasta selecionada: {pasta}"
    )

    ficheiros = procurar_ficheiros(
        pasta
    )

    total = len(ficheiros)

    escrever_log(
        f"Encontrados {total} ficheiros."
    )

    if total == 0:

        escrever_log(
            "Sem ficheiros para converter."
        )

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

        progresso = indice / total

        barra_progresso.set(
            progresso
        )

        escrever_log("")
        escrever_log(
            f"Ficheiro {indice} de {total}"
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
                f"{tempo_ficheiro:.1f} segundos"
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
        f"{tempo_total:.1f} segundos"
    )

    if ultimo_md:

        mostrar_preview(
            ultimo_md
        )


# ==================================================
# INTERFACE
# ==================================================

ctk.set_appearance_mode(
    "dark"
)

ctk.set_default_color_theme(
    "blue"
)

app = ctk.CTk()

app.title(
    "Markdown Converter"
)

app.geometry(
    "1200x750"
)


# ==================================================
# TÍTULO
# ==================================================

titulo = ctk.CTkLabel(
    app,
    text="Conversor para Markdown",
    font=("Arial", 24, "bold")
)

titulo.pack(
    pady=15
)


# ==================================================
# BOTÕES
# ==================================================

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


# ==================================================
# BARRA DE PROGRESSO
# ==================================================

barra_progresso = ctk.CTkProgressBar(
    app
)

barra_progresso.pack(
    fill="x",
    padx=20,
    pady=10
)

barra_progresso.set(0)


# ==================================================
# CRONÓMETRO
# ==================================================

label_tempo = ctk.CTkLabel(
    app,
    text="Tempo decorrido: 00:00:00",
    font=("Arial", 14)
)

label_tempo.pack(
    pady=5
)


# ==================================================
# ÁREA INFERIOR
# ==================================================

frame_principal = ctk.CTkFrame(
    app
)

frame_principal.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=10
)


# ==================================================
# LOG
# ==================================================

frame_log = ctk.CTkFrame(
    frame_principal
)

frame_log.pack(
    side="left",
    fill="both",
    expand=True,
    padx=5
)

ctk.CTkLabel(
    frame_log,
    text="LOG"
).pack(
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


# ==================================================
# PREVIEW
# ==================================================

frame_preview = ctk.CTkFrame(
    frame_principal
)

frame_preview.pack(
    side="left",
    fill="both",
    expand=True,
    padx=5
)

ctk.CTkLabel(
    frame_preview,
    text="PREVIEW MARKDOWN"
).pack(
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


# ==================================================
# INÍCIO
# ==================================================

log.insert(
    "end",
    "Aplicação iniciada...\n"
)

app.mainloop()