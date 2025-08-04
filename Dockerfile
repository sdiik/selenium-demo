FROM python:3.10-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    gnupg \
    ca-certificates \
    chromium \
    chromium-driver \
    fonts-liberation \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    libnss3 \
    libxss1 \
    libasound2 \
    libxrandr2 \
    libgbm1 \
    && rm -rf /var/lib/apt/lists/*

# Set env vars
ENV CHROME_BIN=/usr/bin/chromium
ENV PATH="/usr/lib/chromium/:$PATH"

# Set display to dummy to enable headless
ENV DISPLAY=:99

# Set workdir
WORKDIR /app

# Copy everything into container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
