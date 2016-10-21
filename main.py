# -*- coding: utf-8 -*-
from flask import Flask
from controllers.pdf import html2pdf_controller
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
app = Flask(__name__)
app.register_blueprint(html2pdf_controller)


@app.route('/')
def home():
    return 'HTML2PDF micro service'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
