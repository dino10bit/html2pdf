# -*- coding: utf-8 -*-
import pdfkit
import base64


class Pdf:
    @classmethod
    def html2pdf(cls, html):
        config = pdfkit.configuration(wkhtmltopdf='/app/xwkhtml2pdf')
        pdf_content = pdfkit.from_string(html.encode('UTF-8').decode('UTF-8'), False,
                                         options={'encoding': "UTF-8"}, configuration=config)
        return base64.b64encode(pdf_content)

