import pika
import json

# Настройки RabbitMQ
HOST = 'rabbitmq'
QUEUE_NAME = 'security_monitor_queue'

def send_message(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters(HOST))
    channel = connection.channel()

    # Отправка сообщения в очередь монитора безопасности
    channel.basic_publish(exchange='', routing_key=QUEUE_NAME, body=json.dumps(message))

    connection.close()