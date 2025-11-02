FROM python:3.14-slim

# Install dependencies
RUN apt-get update && apt-get install -y curl

# Install Deno
RUN curl -fsSL https://deno.land/install.sh | sh && \
    ln -s /root/.deno/bin/deno /usr/local/bin/deno

# Set working directory
WORKDIR /app

# Copy requirements first (for Docker cache efficiency)
COPY requirements.txt .

# Install Python dependencies
RUN pip3 install -U pip && pip3 install -U -r requirements.txt

# Copy rest of the app
COPY . .

CMD ["bash", "start"]
