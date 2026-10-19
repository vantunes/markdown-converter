import customtkinter as ctk


class ProgressPanel:

    def __init__(self, parent):

        self.frame = ctk.CTkFrame(parent)

        # Estado

        self.status_label = ctk.CTkLabel(
            self.frame,
            text="Pronto"
        )

        self.status_label.pack(
            pady=(10, 5)
        )

        # Ficheiro atual

        self.file_label = ctk.CTkLabel(
            self.frame,
            text=""
        )

        self.file_label.pack(
            pady=5
        )

        # Cronómetro

        self.timer_label = ctk.CTkLabel(
            self.frame,
            text="Tempo: 00:00:00"
        )

        self.timer_label.pack(
            pady=5
        )

        # Barra progresso

        self.progress_bar = ctk.CTkProgressBar(
            self.frame
        )

        self.progress_bar.pack(
            fill="x",
            padx=20,
            pady=10
        )

        self.progress_bar.set(0)

    # =====================================
    # Atualizar estado
    # =====================================

    def set_status(self, texto):

        self.status_label.configure(
            text=texto
        )

    # =====================================
    # Atualizar ficheiro
    # =====================================

    def set_file(self, texto):

        self.file_label.configure(
            text=texto
        )

    # =====================================
    # Atualizar tempo
    # =====================================

    def set_time(self, texto):

        self.timer_label.configure(
            text=texto
        )

    # =====================================
    # Atualizar progresso
    # =====================================

    def set_progress(self, valor):

        self.progress_bar.set(
            valor
        )

    # =====================================
    # Widget principal
    # =====================================

    def get_widget(self):

        return self.frame

