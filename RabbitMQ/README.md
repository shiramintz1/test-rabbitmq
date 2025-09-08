# RabbitMQ

    This RabbitMQ package is for use to communicate between the various services.It provides a simple and convenient way to send and receive messages between applications or microservices.

## Installation:

    The binary installation file attached to this repository should be taken, Attach to the project where it will be used and install with:
    pip install path/to/rabbitmq-0.1.0-py3-none-any.whl

    Replace path/to/rabbitmq-0.1.0-py3-none-any.whl with the path where the file is located in your project.

## Usage

    To use the rabbitMQ library, follow these steps:
    First of all you need to get the host of your Rabbit application.
    To run a Rabbit image on Docker you need to run this command:

    docker run -it --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.12-management
    This will run a RabbitMQ container exposing the AMQP port (5672) and the management HTTP port (15672). Take note of the IP address where RabbitMQ is running, usually localhost.

## Then run:

    docker inspect<id-of-rabbitmq-container>
    Looking for the IPAddress, and keep this. It will be used as the RabbitMQ host.

    Notice that this package supports default values of host, port, username and password. python  host="localhost", port=5672, username="guest", password="guest",

## Import the rabbitMQ class:

    from rabbitmq import Producer from rabbitmq import Consumer

## Create a Producer and Consumer instance, you should send the queue name:

## producer

    rabbitmq_url = os.getenv("RABBITMQ_URL", "amqp://       guest:guest@rabbitmq:5672/")
    parsed = pika.URLParameters(rabbitmq_url)

    p = Producer(
        queue_name="my_queue",
        host=parsed.host,
        port=parsed.port,
        username=parsed.credentials.username,
        password=parsed.credentials.password
    )
    p.publish({"msg": "Hello from Docker!"})
    p.connection.close()

## Use to consume messages from RabbitMQ You should send a callback function to get the message details:

    def message_received_callback(message):
    print("Received message:", message)

## consumer

    rabbitmq_url = os.getenv("RABBITMQ_URL", "amqp://guest:guest@rabbitmq:5672/")
    parsed = pika.URLParameters(rabbitmq_url)

    consumer = Consumer(
        queue_name="my_queue",
        callback=message_received_callback,
        error_queue_name="errors_queue",
        host=parsed.host,
        port=parsed.port,
        username=parsed.credentials.username,
        password=parsed.credentials.password
    )
    consumer.consume()

## Failed Messages

information if a message fails processing (throws an exception), It should be sent to the "errors_queue" queue.
