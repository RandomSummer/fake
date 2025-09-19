# Base image
FROM python:3.12-slim

# Set work directory
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y build-essential libpq-dev && rm -rf /var/lib/apt/lists/*

# Install pip requirements
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project
COPY . .

# Default command: run gunicorn
CMD ["gunicorn", "form_project.wsgi:application", "--bind", "0.0.0.0:8000"]
