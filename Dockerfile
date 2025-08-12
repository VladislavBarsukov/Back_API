FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir allure-pytest

RUN apt-get update
RUN apt-get install -y wget unzip
RUN wget https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.25.0/allure-commandline-2.25.0.zip -O allure.zip
RUN unzip allure.zip -d /opt
RUN ln -s /opt/allure-commandline-2.25.0/bin/allure /usr/local/bin/allure

COPY . .
CMD ["pytest", "-sv"]