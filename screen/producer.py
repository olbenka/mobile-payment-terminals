import pika
import json

HOST = 'rabbitmq'

def send_message(routing_key, message):
    connection = pika.BlockingConnection(pika.ConnectionParameters(HOST))
    channel = connection.channel()

    # Отправка сообщения в очередь микросервиса
    channel.basic_publish(exchange='', routing_key=routing_key, body=json.dumps(message))

    connection.close()
