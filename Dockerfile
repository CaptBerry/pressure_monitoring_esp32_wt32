# Базовый образ
FROM python:3.11-slim

# Установка зависимостей системы
RUN apt-get update && apt-get install -y build-essential libpq-dev curl && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .

# Установка зависимостей Python
RUN pip install --no-cache-dir -r requirements.txt

# Копирование проекта
COPY . .

# Dockerfile (пример последних строк)
RUN python manage.py collectstatic --noinput

# Указание команды по умолчанию
CMD ["gunicorn", "dashboard.wsgi:application", "--bind", "0.0.0.0:8000"]
