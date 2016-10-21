FROM ubuntu:14.04
MAINTAINER Wei Zhang "wzhang@ancoris.com"
RUN apt-get update -y
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential wget xvfb
RUN wget https://bitbucket.org/wkhtmltopdf/wkhtmltopdf/downloads/wkhtmltox-0.13.0-alpha-7b36694_linux-trusty-amd64.deb -O wkhtmltox.deb
RUN apt-get install -y gdebi-core
RUN gdebi --non-interactive wkhtmltox.deb
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["main.py"]
