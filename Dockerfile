FROM python:3.5
RUN apt-get update && apt-get install -y \
    libpq-dev
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN pip install -r requirements.txt
EXPOSE 8000
