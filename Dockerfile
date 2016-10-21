FROM ubuntu:latest
MAINTAINER Wei Zhang "wzhang@ancoris.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential wkhtmltopdf
RUN apt-get install -y xvfb
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV DISPLAY :0
ENTRYPOINT ["bash"]
CMD ["start.sh"]
