import json
import pika
from .connection import create_connection

class Consumer:
    def __init__(self, queue_name, callback, error_queue_name, host, port, username, password):
        self.queue_name = queue_name
        self.callback = callback
        self.error_queue_name = error_queue_name

        self.connection = create_connection(host, port, username, password)
        self.channel = self.connection.channel()

        # Create main and error queues
        self.channel.queue_declare(queue=queue_name, durable=True)
        self.channel.queue_declare(queue=error_queue_name, durable=True)

    def consume(self):
        def internal_callback(ch, method, properties, body):
            try:
                message = json.loads(body)
                print(f"[Consumer] Received message: {message}!!")
                self.callback(message)
                ch.basic_ack(delivery_tag=method.delivery_tag)
                print("[Consumer] Message acknowledged")
            except Exception as e:
                print(f"[Consumer] Error handling message: {e}")
                self.channel.basic_publish(
                    exchange='',
                    routing_key=self.error_queue_name,
                    body=body,
                    properties=pika.BasicProperties(delivery_mode=2)
                )
                ch.basic_ack(delivery_tag=method.delivery_tag)

        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(queue=self.queue_name, on_message_callback=internal_callback)
        print("[Consumer] Waiting for messages...")
        self.channel.start_consuming()

def message_received_callback(message):
    print(f"[Callback] Processing message: {message}")
