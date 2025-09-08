import json
import pika
from .connection import create_connection  

class Producer:
    def __init__(self, queue_name, host, port, username, password):
        self.queue_name = queue_name
        self.connection = create_connection(host, port, username, password)
        self.channel = self.connection.channel()
     
        self.channel.queue_declare(queue=queue_name, durable=True)

    def publish(self, message: dict):
        body = json.dumps(message)
        self.channel.basic_publish(
            exchange='',
            routing_key=self.queue_name,
            body=body,
            properties=pika.BasicProperties(delivery_mode=2)  # make message persistent
        )
        print(f"[Producer] Sent message: {body}")
