import threading

from tkinter import filedialog

from services.conversion_service import (
    ConversionService
)

from services.update_service import (
    UpdateService
)

from services.timer_service import TimerService

import customtkinter as ctk

from settings import (
    APP_NOME,
    APP_VERSAO,
    APP_TEMA,
    APP_COR,
    JANELA_LARGURA,
    JANELA_ALTURA
)

from ui.toolbar import Toolbar
from ui.log_panel import LogPanel
from ui.preview_panel import PreviewPanel
from ui.progress_panel import ProgressPanel
from ui.about_dialog import AboutDialog



class MainWindow:

    def __init__(self):

        ctk.set_appearance_mode(APP_TEMA)
        ctk.set_default_color_theme(APP_COR)

        self.app = ctk.CTk()

        self.app.title(
            f"{APP_NOME} v{APP_VERSAO}"
        )

        self.app.geometry(
            f"{JANELA_LARGURA}x{JANELA_ALTURA}"
        )

        self.converter = ConversionService()

        self.updater = UpdateService()

        self.create_interface()

        self.timer = TimerService()

        self.timer_running = False

    def create_interface(self):

        titulo = ctk.CTkLabel(
            self.app,
            text=f"{APP_NOME} v{APP_VERSAO}",
            font=("Arial", 24, "bold")
        )

        titulo.pack(pady=20)

        self.toolbar = Toolbar(
            self.app,
            on_file=self.on_file,
            on_folder=self.on_folder,
            on_update=self.on_update,
            on_about=self.on_about
        )

        self.toolbar.get_widget().pack(
            fill="x",
            padx=20,
            pady=10
        )

        self.progress = ProgressPanel(
            self.app
        )

        self.progress.get_widget().pack(
            fill="x",
            padx=20,
            pady=10
        )

        content = ctk.CTkFrame(
            self.app
        )

        content.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        self.log = LogPanel(content)

        self.log.get_widget().pack(
            side="left",
            fill="both",
            expand=True,
            padx=5
        )

        self.preview = PreviewPanel(content)

        self.preview.get_widget().pack(
            side="left",
            fill="both",
            expand=True,
            padx=5
        )

        self.log.write(
            "Aplicação iniciada."
        )
    def update_timer(self):

        if self.timer_running:

            tempo = self.timer.elapsed_precise()

            self.progress.set_time(
                f"Tempo: {tempo:.1f} s"
            )

            self.app.after(
                100,
                self.update_timer
            )
    # =========================
    # EVENTOS
    # =========================

    def on_file(self):

        ficheiro = filedialog.askopenfilename()

        if not ficheiro:
            return

        thread = threading.Thread(

            target=self.convert_file_thread,

            args=(ficheiro,),

            daemon=True

        )

        thread.start()

###
    def convert_file_thread(
        self,
        ficheiro
    ):

        self.log.write("")
        self.log.write(
            "Ficheiro selecionado:"
        )

        self.log.write(
            ficheiro
        )
        self.progress.set_time(
            "Tempo: 0.0 s"
        )
        self.timer.start()

        self.timer_running = True

        self.update_timer()

        import time
        time.sleep(5)

        try:

            resultado = self.converter.convert_file(
                ficheiro
            )

            self.timer_running = False

            self.log.write(
                "[OK] Conversão concluída."
            )

            self.log.write(
                f"Tempo: "
                f"{resultado['elapsed']:.2f} s"
            )

            self.preview.show_file(
                resultado["output"]
            )

            self.progress.set_progress(1)

            self.progress.set_status(
                "Concluído"
            )

            self.progress.set_file(
                resultado["output"]
            )

        except Exception as erro:

            self.timer_running = False

            self.log.write(
                f"[ERRO] {erro}"
            )
###

    def on_folder(self):

        pasta = filedialog.askdirectory()

        if not pasta:
            return

        thread = threading.Thread(

            target=self.convert_folder_thread,

            args=(pasta,),

            daemon=True

        )

        thread.start()
    def folder_progress_callback(

        self,

        indice,

        total,

        resultado

    ):

        progresso = indice / total

        self.progress.set_progress(
            progresso
        )

        self.progress.set_status(
            f"Ficheiro {indice} de {total}"
        )

        if resultado["success"]:

            self.log.write(

                f"[OK] "

                f"{resultado['output']}"

            )

        else:

            self.log.write(

                f"[ERRO] "

                f"{resultado['source']}"

            )
    def convert_folder_thread(

        self,

        pasta

    ):

        try:

            self.log.write("")

            self.log.write(

                f"Pasta selecionada: "

                f"{pasta}"

            )

            self.progress.set_progress(0)

            self.progress.set_status(
                "Conversão iniciada"
            )
            self.progress.set_time(
                "Tempo: 0.0 s"
            )
            
            self.timer.start()

            self.timer_running = True

            self.update_timer()
            resultado = (

                self.converter.convert_folder(

                    pasta,

                    self.folder_progress_callback

                )

            )

            self.progress.set_progress(1)

            self.progress.set_status(
                "Concluído"
            )

            self.log.write("")

            self.log.write(
                "[OK] Conversão concluída."
            )

            self.log.write(

                f"Tempo total: "

                f"{resultado['total_time']:.2f} s"

            )

            # Mostrar último markdown

            if resultado["results"]:

                ultimo = (

                    resultado["results"][-1]

                )

                if ultimo["success"]:

                    self.preview.show_file(

                        ultimo["output"]

                    )

        except Exception as erro:

            self.log.write(

                f"[ERRO] {erro}"

            )
    def on_update(self):

        self.log.write("")
        self.log.write(
            "Verificação de atualizações iniciada..."
        )

        try:

            self.updater.update(
                self.log.write
            )

        except Exception as erro:

            self.log.write(
                f"[ERRO] {erro}"
            )

    def on_about(self):

        AboutDialog.show()

    # =========================
    # MAINLOOP
    # =========================

    def run(self):

        self.app.mainloop()