import pika
import json
from producer import send_message

HOST = 'rabbitmq'
QUEUE_NAME = 'control_input_queue'

def on_message(ch, method, properties, body):
    message = json.loads(body.decode())
    message_id = message.get('id')
    details = message.get('details')

    print(f'[info] Control Input received message {message_id}: {details}')

    # Отправляем сообщение в central через монитор безопасности
    message = {
        'id': 'control_input_data',
        'details': {
            'source': 'control_input',
            'deliver_to': 'central',
            'operation': 'send_keyboard_input',
            'amount': details.get('amount')
        }
    }
    send_message('security_monitor_queue', message)
    print(f'[info] Sent message to security_monitor_queue: {message}')

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(HOST))
    channel = connection.channel()

    channel.queue_declare(queue=QUEUE_NAME)
    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=on_message, auto_ack=True)

    print('Control Input is listening...')
    channel.start_consuming()

if __name__ == '__main__':
    main()
