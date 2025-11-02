FROM python:3.14-slim

# Install curl for Deno installation (if needed)
RUN apt-get update && apt-get install -y curl

# Install Deno (if your project also uses Deno)
RUN curl -fsSL https://deno.land/install.sh | sh && \
    ln -s /root/.deno/bin/deno /usr/local/bin/deno

# Set working directory
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip3 install -U pip && pip3 install -U -r requirements.txt

# Copy all project files into the image
COPY . .

# Default command to start your app
CMD ["python3", "-m", "anony"]
