import pika
import json
from producer import send_message

HOST = 'rabbitmq'
QUEUE_NAME = 'screen_queue'

def on_message(ch, method, properties, body):
    message = json.loads(body.decode())
    message_id = message.get('id')
    details = message.get('details')

    print(f'[info] Screen received message {message_id}: {details}')

    # Обработка сообщений от central
    if details['operation'] == 'authorize_transaction':
        amount = details.get('amount')
        print(f"Авторизация транзакции на сумму {amount}...")

    

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(HOST))
    channel = connection.channel()

    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=on_message, auto_ack=True)

    print('Screen is listening...')
    channel.start_consuming()

if __name__ == '__main__':
    main()