FROM python:3
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y gettext
WORKDIR /mnt
ADD . /mnt/
