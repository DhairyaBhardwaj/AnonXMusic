FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip3 install -U pip && pip3 install -U -r requirements.txt

COPY . .

# Make sure ffmpeg is available
RUN apt-get update && apt-get install -y ffmpeg

# Start your bot
CMD ["python3", "-m", "anony"]
