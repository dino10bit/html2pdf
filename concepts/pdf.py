# -*- coding: utf-8 -*-
import pdfkit
import base64
import tempfile
import os
import subprocess
import settings


class Pdf:
    def __init__(self, html, pin=''):
        self.html = html
        self.pin = pin
        self.pdf_file = None
        self.pdf_file_encrypted = None

    def html2pdf(self):
        self.pdf_file = tempfile.NamedTemporaryFile()

        config = pdfkit.configuration(wkhtmltopdf=settings.WKHTMLTOPDF_PATH)
        pdfkit.from_string(self.html.encode('UTF-8').decode('UTF-8'), self.pdf_file.name,
                           configuration=config)
        output_file = self.apply_security()
        file_content = open(output_file).read()
        self.clean_up()
        return base64.b64encode(file_content)

    def apply_security(self):
        if not self.pin or not self.pdf_file:
            return self.pdf_file.name

        self.pdf_file_encrypted = tempfile.NamedTemporaryFile()
        subprocess.call(['qpdf', '--encrypt', self.pin, self.pin, '128', '--use-aes=y', '--', self.pdf_file.name,
                         self.pdf_file_encrypted.name])

        return self.pdf_file_encrypted.name

    def clean_up(self):
        if self.pdf_file:
            os.unlink(self.pdf_file.name)
        if self.pdf_file_encrypted:
            os.unlink(self.pdf_file_encrypted.name)
