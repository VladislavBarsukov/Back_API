FROM python:3.12-bullseye

# Установка Java (требуется для Allure)
RUN apt-get update && apt-get install -y openjdk-11-jre-headless wget unzip && \
    apt-get clean

# Установка переменной окружения для Java
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH=$PATH:$JAVA_HOME/bin

# Установка Allure CLI
RUN wget -O /tmp/allure.zip -L https://github.com/allure-framework/allure2/releases/download/2.34.1/allure-2.34.1.zip && \
    unzip /tmp/allure.zip -d /opt/ && \
    ln -s /opt/allure-2.34.1/bin/allure /usr/local/bin/allure

# Рабочая директория
WORKDIR /back_api

# Копирование зависимостей и установка
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование проекта
COPY . .

# Команда по умолчанию для запуска тестов
CMD ["pytest", "-sv", "--alluredir=allure-results"]