from converter import converter_ficheiro
from file_scanner import procurar_ficheiros

from services.timer_service import TimerService


class ConversionService:

    def __init__(self):

        self.timer = TimerService()

    # =====================================
    # CONVERSÃO DE UM FICHEIRO
    # =====================================

    def convert_file(
        self,
        file_path
    ):

        self.timer.start()

        md_file = converter_ficheiro(
            file_path
        )

        elapsed = (
            self.timer.elapsed_precise()
        )

        return {

            "success": True,

            "source": file_path,

            "output": str(md_file),

            "elapsed": elapsed

        }

    # =====================================
    # CONVERSÃO DE UMA PASTA
    # =====================================

    def convert_folder(
        self,
        folder_path,
        progress_callback=None
    ):

        files = procurar_ficheiros(
            folder_path
        )

        total = len(files)

        results = []

        total_timer = TimerService()

        total_timer.start()

        for index, file_path in enumerate(
            files,
            start=1
        ):

            file_timer = TimerService()

            file_timer.start()

            try:

                md_file = converter_ficheiro(
                    file_path
                )

                elapsed_file = (
                    file_timer.elapsed_precise()
                )

                result = {

                    "success": True,

                    "index": index,

                    "total": total,

                    "source": str(file_path),

                    "output": str(md_file),

                    "elapsed": elapsed_file

                }

            except Exception as error:

                elapsed_file = (
                    file_timer.elapsed_precise()
                )

                result = {

                    "success": False,

                    "index": index,

                    "total": total,

                    "source": str(file_path),

                    "error": str(error),

                    "elapsed": elapsed_file

                }

            results.append(result)

            if progress_callback:

                progress_callback(
                    index,
                    total,
                    result
                )

        total_elapsed = (
            total_timer.elapsed_precise()
        )

        return {

            "total_files": total,

            "total_time": total_elapsed,

            "results": results

        }