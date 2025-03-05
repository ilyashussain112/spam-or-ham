FROM python:3.10-slim

WORKDIR /app

COPY requairment.txt .

RUN pip install -r requairment.txt

COPY . .

EXPOSE 5000

ENV PYTHONUNBUFFERED=1

CMD [ "python", "app.py" ]