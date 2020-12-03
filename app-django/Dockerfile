FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /app-django
WORKDIR /app-django
COPY requirements.txt /app-django/
RUN pip install -r requirements.txt
COPY . /app-django/