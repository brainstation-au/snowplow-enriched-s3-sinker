FROM python:slim as prod

RUN apt-get update -y && apt-get install -y git zip

WORKDIR /opt/code


FROM prod as test

COPY ./requirements.txt ./requirements_dev.txt /tmp/

RUN pip install -r /tmp/requirements_dev.txt
