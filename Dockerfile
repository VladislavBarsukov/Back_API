FROM python:3.12-bullseye

WORKDIR /back_api

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["pytest", "-sv"]