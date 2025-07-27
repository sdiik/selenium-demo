FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

ENV CHROME_BIN=/usr/bin/chromium
ENV PATH="/usr/lib/chromium/:$PATH"

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt