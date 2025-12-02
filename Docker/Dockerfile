# docker/Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY scripts/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY scripts/app.py /app/app.py
COPY data /app/data

ENV DATA_PATH=/app/data/input.csv
EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app", "--workers", "1"]
