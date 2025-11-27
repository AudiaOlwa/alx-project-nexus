# Lightweight Python image
FROM python:3.11-slim

# Prevents Python from writing cache files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt
RUN pip install --upgrade pip

# Copy source code
COPY requirements.txt .

# Start Gunicorn server
CMD ["gunicorn","ecommerce.wsgi:application","--bind","0.0.0.0:8000"]
