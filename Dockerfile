FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# опируем С файлы
COPY . .

# роверяем что файлы скопировались
RUN echo "=== Files in container ==="
RUN ls -la
RUN echo "=== Python files ==="
RUN find . -name "*.py" | head -10

# апускаем тесты TODO
CMD python -m pytest test_todo.py -v
