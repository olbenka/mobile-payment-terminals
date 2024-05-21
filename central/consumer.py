import pika
import json
from producer import send_message

HOST = '127.0.0.1'
QUEUE_NAME = 'central_queue'

def on_message(ch, method, properties, body):
    message = json.loads(body.decode())
    message_id = message.get('id')
    details = message.get('details')

    print(f'[info] Central received message {message_id}: {details}')

    # Обработка сообщений от control_input
    if details['operation'] == 'send_keyboard_input':
        amount = details.get('amount')
        print(f"Сумма, полученная от control_input: {amount}")

        # Отправляем сообщение в screen
        message = {
            'id': 'authorize_purchase',
            'details': {
                'source': 'central',
                'deliver_to': 'screen',
                'operation': 'authorize_transaction',
                'amount': amount
            }
        }
        send_message('security_monitor_queue', message)

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(HOST))
    channel = connection.channel()

    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=on_message, auto_ack=True)

    print('Central is listening...')
    channel.start_consuming()

if __name__ == '__main__':
    main()