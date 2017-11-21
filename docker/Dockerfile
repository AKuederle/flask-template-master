FROM akuederle/docker-latex-python:latest

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt --upgrade

ADD docker /docker

WORKDIR /opt/project
EXPOSE  5000
ENTRYPOINT ["/docker/entrypoint.sh"]