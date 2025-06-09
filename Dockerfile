# Use official Python base image
FROM python:3.11-slim

# Set work directory inside container
WORKDIR /app

# Install system dependencies (for psycopg2 and Redis)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port for daphne
EXPOSE 8000

# Run migrations and start Daphne server (can be overridden in docker-compose)
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "whiteboard_project.asgi:application"]
