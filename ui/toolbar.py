import customtkinter as ctk


class Toolbar:

    def __init__(
        self,
        parent,
        on_file=None,
        on_folder=None,
        on_update=None,
        on_about=None
    ):

        self.frame = ctk.CTkFrame(parent)

        self.btn_file = ctk.CTkButton(
            self.frame,
            text="Selecionar Ficheiro",
            command=on_file
        )

        self.btn_file.pack(
            side="left",
            padx=5,
            pady=10
        )

        self.btn_folder = ctk.CTkButton(
            self.frame,
            text="Selecionar Pasta",
            command=on_folder
        )

        self.btn_folder.pack(
            side="left",
            padx=5,
            pady=10
        )

        self.btn_update = ctk.CTkButton(
            self.frame,
            text="Atualizar Dependências",
            command=on_update
        )

        self.btn_update.pack(
            side="left",
            padx=5,
            pady=10
        )

        self.btn_about = ctk.CTkButton(
            self.frame,
            text="Sobre",
            command=on_about
        )

        self.btn_about.pack(
            side="right",
            padx=5,
            pady=10
        )

    def get_widget(self):

        return self.frame