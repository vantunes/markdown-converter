import customtkinter as ctk


class PreviewPanel:

    def __init__(self, parent):

        self.frame = ctk.CTkFrame(parent)

        self.label = ctk.CTkLabel(
            self.frame,
            text="PREVIEW MARKDOWN"
        )

        self.label.pack(
            pady=5
        )

        self.textbox = ctk.CTkTextbox(
            self.frame
        )

        self.textbox.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

    def show_text(self, texto):

        self.textbox.delete(
            "1.0",
            "end"
        )

        self.textbox.insert(
            "end",
            texto
        )

    def show_file(self, ficheiro_md):

        try:

            with open(
                ficheiro_md,
                "r",
                encoding="utf-8"
            ) as f:

                conteudo = f.read()

            self.show_text(
                conteudo
            )

        except Exception as erro:

            self.show_text(
                f"Erro ao abrir ficheiro:\n\n{erro}"
            )

    def clear(self):

        self.textbox.delete(
            "1.0",
            "end"
        )

    def get_widget(self):

        return self.frame