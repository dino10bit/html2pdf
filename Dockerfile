FROM ubuntu:latest
MAINTAINER Wei Zhang "wzhang@ancoris.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential wkhtmltopdf
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["main.py"]