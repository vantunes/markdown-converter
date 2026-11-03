import os
import tempfile

import ocrmypdf


class OCRService:

    @staticmethod
    def process_pdf(pdf_path):

        nome = os.path.basename(pdf_path)

        output_pdf = os.path.join(
            tempfile.gettempdir(),
            f"ocr_{nome}"
        )

        try:

            ocrmypdf.ocr(
                pdf_path,
                output_pdf,
                language="por",
                skip_text=True,
                deskew=True,
                optimize=1,
                progress_bar=False
            )

            return output_pdf

        except Exception as error:

            print(f"Erro OCR: {error}")

            return pdf_path