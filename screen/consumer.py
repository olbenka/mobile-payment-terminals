import pika
import json
import redis

HOST = 'rabbitmq'
REDIS_HOST = 'redis'
QUEUE_NAME = 'screen_queue'

r = redis.Redis(host=REDIS_HOST, port=6379, db=0)

def on_message(ch, method, properties, body):
    print('[info] Received a message')
    try:
        message = json.loads(body.decode())
        message_id = message.get('id')
        details = message.get('details')

        print(f'[info] Screen received message {message_id}: {details}')

        # Сохраняем сообщение в Redis
        r.rpush('messages', json.dumps(details))
        print(f'[info] Current messages: {r.lrange("messages", 0, -1)}')
    except Exception as e:
        print(f'[error] Failed to process message: {e}')

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(HOST))
    channel = connection.channel()

    channel.queue_declare(queue=QUEUE_NAME)
    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=on_message, auto_ack=True)

    print('Screen is listening...')
    channel.start_consuming()

if __name__ == '__main__':
    main()
