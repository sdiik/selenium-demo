# Gunakan Python base image
FROM python:3.10-slim

# Install Chrome & ChromeDriver
RUN apt-get update && apt-get install -y \
    chromium chromium-driver \
    curl unzip gnupg2 \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Set environment path agar selenium bisa akses Chrome & driver
ENV PATH="/usr/lib/chromium/:$PATH"
ENV CHROME_BIN="/usr/bin/chromium"
ENV CHROMEDRIVER_PATH="/usr/lib/chromium/chromedriver"

# Setup folder kerja
WORKDIR /app
COPY . .