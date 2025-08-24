FROM python:3.12-bullseye

WORKDIR /back_api

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y wget unzip openjdk-11-jre

RUN wget -O /tmp/allure.zip https://github.com/allure-framework/allure2/releases/download/2.24.0/allure-2.24.0.zip && \
    unzip /tmp/allure.zip -d /opt/ && \
    ln -s /opt/allure-2.24.0/bin/allure /usr/local/bin/allure && \
    rm /tmp/allure.zip

COPY . /back_api

CMD ["pytest", "-sv", "--alluredir=allure-results"]