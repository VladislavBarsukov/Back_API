FROM python:3.12-slim

WORKDIR /back_api

COPY requirements.txt .
RUN pip install --upgrade --no-cache-dir -r requirements.txt

COPY . /back_api

CMD ["pytest", "-sv"]