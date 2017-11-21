FROM python:3.5

EXPOSE  5000

RUN apt-get update && apt-get install -y texlive-full
RUN rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt --upgrade

ADD docker /docker

WORKDIR /opt/project
ENTRYPOINT ["/docker/entrypoint.sh"]