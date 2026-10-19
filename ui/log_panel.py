import customtkinter as ctk


class LogPanel:

    def __init__(self, parent):

        self.frame = ctk.CTkFrame(parent)

        self.label = ctk.CTkLabel(
            self.frame,
            text="LOG"
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

    def write(self, texto):

        self.textbox.insert(
            "end",
            texto + "\n"
        )

        self.textbox.see("end")

    def clear(self):

        self.textbox.delete(
            "1.0",
            "end"
        )

    def get_widget(self):

        return self.frame