FROM python:3.10

WORKDIR /docker_compose

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

COPY requirements.txt requirements.txt

RUN  pip install --upgrade pip && pip install -r requirements.txt

COPY ./app/ .

EXPOSE 8000

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000" ]
