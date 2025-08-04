FROM python:3.10-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
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

# Install Allure CLI
RUN curl -Lo allure.tgz https://github.com/allure-framework/allure2/releases/download/2.27.0/allure-2.27.0.tgz \
    && tar -xzf allure.tgz \
    && mv allure-2.27.0 /opt/allure-2.27.0 \
    && chmod +x /opt/allure-2.27.0/bin/allure \
    && ln -s /opt/allure-2.27.0/bin/allure /usr/bin/allure \
    && rm allure.tgz

# Set workdir
WORKDIR /app

# Copy everything into container
COPY . .

# Install Java (required by Allure)
RUN apt-get update && apt-get install -y openjdk-11-jdk
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH="${JAVA_HOME}/bin:${PATH}"

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
