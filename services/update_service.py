from updater import atualizar_dependencias


class UpdateService:

    def __init__(self):

        pass

    def update(self, log_callback):

        atualizar_dependencias(
            log_callback
        )