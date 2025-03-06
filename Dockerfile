FROM python:3.10-slim

WORKDIR /app

COPY requairment.txt .

RUN pip install --upgrade pip

RUN pip install -r requairment.txt

COPY . .

EXPOSE 5000


CMD [ "python", "app.py" ]