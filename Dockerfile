FROM python:3.12-slim

# Установка Poetry
RUN pip install --no-cache-dir poetry

# Рабочая директория
WORKDIR /api

# Копируем зависимости
COPY pyproject.toml poetry.lock* ./

# Установка зависимостей без создания виртуального окружения
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Копируем всё остальное
COPY . .

# Открываем порт
EXPOSE 8000

# Запуск FastAPI
CMD ["poetry", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
