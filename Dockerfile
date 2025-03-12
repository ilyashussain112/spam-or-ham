FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

# RUN apt-get update && apt-get install -y git pkg-config default-mysql-client libmariadb-dev gcc python3-dev

RUN pip install --no-cache-dir -r requirements.txt
COPY models /app/models
COPY . .

EXPOSE 5000

ENV PYTHONUNBUFFERED=1

CMD ["python", "app.py"]
