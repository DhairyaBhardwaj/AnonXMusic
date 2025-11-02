FROM python:3.14-slim

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -U pip && pip3 install -U -r requirements.txt

COPY . .
RUN chmod +x start

CMD ["python3", "-m", "anony"]
