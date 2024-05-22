import pika
import json
import base64
from policies import check_operation

HOST = 'rabbitmq'
QUEUE_NAME = 'security_monitor_queue'

def on_message(ch, method, properties, body):
    message = json.loads(body.decode())
    message_id = message.get('id')
    details = message.get('details')

    print(f'[info] Monitor received message {message_id}: {details}')

    if check_operation(message_id, details):
        print(f'[info] Message {message_id} is authorized')
        routing_key = details['deliver_to']
        print(f'[info] Routing message to {routing_key}')
        ch.basic_publish(exchange='', routing_key=routing_key, body=json.dumps(message))
    else:
        print(f'[error] Message {message_id} is unauthorized. Details: {details}')
        with open('security_log.txt', 'a') as f:
            f.write(f'[error] Unauthorized message: {json.dumps(message)}\n')

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(HOST))
    channel = connection.channel()

    channel.queue_declare(queue=QUEUE_NAME)
    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=on_message, auto_ack=True)

    print('Security Monitor is listening...')
    channel.start_consuming()

if __name__ == '__main__':
    main()
