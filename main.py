from flask import Flask
from controllers.pdf import html2pdf_controller

app = Flask(__name__)
app.register_blueprint(html2pdf_controller)


@app.route('/')
def home():
    return 'HTML2PDF micro service'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
