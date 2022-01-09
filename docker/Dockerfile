FROM python:3.9.1

RUN apt-get update && apt-get install -yy gcc build-essential python-setuptools graphviz libgraphviz-dev

ENV PYTHONUNBUFFERED 1

# Install inotify for gunicorn to nicely reload things..
RUN apt-get update && apt-get install -y inotify-tools gdal-bin

ADD requirements/common.txt .
ADD requirements/dev.txt .

# Installing the dependencies
RUN pip install --upgrade pip
RUN pip install -r dev.txt

WORKDIR /app

ENV PYTHONPATH "${PYTHONPATH}:/app/src"
