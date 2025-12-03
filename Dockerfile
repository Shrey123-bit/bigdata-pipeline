FROM python:3.10

WORKDIR /app

COPY scripts/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY data/input.csv input.csv
COPY scripts/app.py app.py

CMD ["python", "app.py"]
