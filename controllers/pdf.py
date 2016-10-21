# -*- coding: utf-8 -*-
from flask import Blueprint, request, jsonify
from concepts.pdf import Pdf
import base64
import logging

html2pdf_controller = Blueprint('html2pdf', __name__)


@html2pdf_controller.route('/html2pdf', methods=['POST'])
def post():
    try:
        json_data = request.get_json(force=True)
        base64_pdf_string = Pdf.html2pdf(base64.decodestring(json_data['base64_html']))
        return jsonify({'base64_pdf': base64_pdf_string})
    except Exception as ex:
        logging.error(ex)
        return jsonify({'error': repr(ex)})
