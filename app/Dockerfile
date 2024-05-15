# базовый образ Python
FROM python:3.9

# рабочая директория в контейнере
WORKDIR /app

# зависимости
COPY requirements.txt .

# Установите зависимости в виртуальное окружение
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --upgrade pip && pip install -r requirements.txt

# Скопируйте остальные файлы проекта
COPY . .

# Укажите порт, который будет слушать ваш сервер
EXPOSE 8000

# Запустите сервер FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]