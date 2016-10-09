import pdfkit
import base64


class Pdf:
    @classmethod
    def html2pdf(cls, html):
        pdf_content = pdfkit.from_string(html, False)
        return base64.encodestring(pdf_content)

