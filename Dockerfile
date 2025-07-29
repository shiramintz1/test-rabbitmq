FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1  
ENV PYTHONUNBUFFERED=1         

RUN pip install --upgrade pip

WORKDIR /app
COPY . /app

RUN pip install .

CMD ["python", "-m", "RabbitMQ.producer"]

