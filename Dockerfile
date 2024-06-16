FROM python:3.12

ENV PYTHONUNBUFFERED 1

COPY . /opt
WORKDIR /opt
RUN pip install poetry

RUN poetry export --format requirements.txt --output requirements.txt
RUN pip install -r requirements.txt

WORKDIR /opt/b2brokertest
EXPOSE 8000
