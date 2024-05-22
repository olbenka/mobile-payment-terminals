import pika
import json
from producer import send_message

HOST = 'rabbitmq'
QUEUE_NAME = 'keyboard_queue'

def on_message(ch, method, properties, body):
    message = json.loads(body.decode())
    message_id = message.get('id')
    details = message.get('details')

    print(f'[info] Keyboard received message {message_id}: {details}')

    amount = details.get('amount')
    print(f"Сумма, введенная с клавиатуры: {amount}")

    # Отправляем сообщение в control_input через монитор
    message = {
        'id': 'keyboard_data',
        'details': {
            'source': 'keyboard',
            'deliver_to': 'control_input',
            'operation': 'send_keyboard_input',
            'amount': amount
        }
    }
    send_message('security_monitor_queue', message)

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(HOST))
    channel = connection.channel()

    channel.queue_declare(queue=QUEUE_NAME)
    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=on_message, auto_ack=True)

    print('Keyboard is listening...')
    channel.start_consuming()

if __name__ == '__main__':
    main()
