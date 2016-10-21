FROM ubuntu:latest
MAINTAINER Wei Zhang "wzhang@ancoris.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential wkhtmltopdf
RUN apt-get install -y xvfb
ADD multiverse.list /etc/apt/sources.list.d/multiverse.list
RUN apt-get update -y
RUN echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select true | debconf-set-selections
RUN apt-get install --no-install-recommends -y -q ttf-mscorefonts-installer
RUN fc-cache -fv
RUN apt-get install -y qpdf
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV DISPLAY :0
ENTRYPOINT ["bash"]
CMD ["start.sh"]
