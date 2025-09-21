FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# (build tools are small; helpful even if you stay on SQLite)
RUN apt-get update && apt-get install -y --no-install-recommends \
      build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# copy project
COPY . .

# run with gunicorn on port 8000
CMD ["gunicorn", "form_project.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
