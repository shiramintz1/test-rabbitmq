import pika

def create_connection(host, port, username, password):
    credentials = pika.PlainCredentials(username, password)
    parameters = pika.ConnectionParameters(host=host, port=port, credentials=credentials)
    return pika.BlockingConnection(parameters)
