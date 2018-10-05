FROM python:3.7-alpine3.7

COPY ./requirements.txt /requirements.txt

RUN pip3 install -r /requirements.txt

COPY ./app /app

WORKDIR /app

RUN pytest

CMD [ "python", "app.py" ]