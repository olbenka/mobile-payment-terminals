# from aio_pika import connect_robust, IncomingMessage
# from asyncio import get_event_loop
# from json import loads
# from policies import check_operation

# async def consume(message: IncomingMessage):
#     async with message.process():
#         try:
#             payload = loads(message.body.decode())
#             src = payload.get('source', '')
#             dst = payload.get('destination', '')
#             operation = payload.get('operation', '')
#             if check_operation(src, dst, operation):
#                 print("Authorized message received:", payload)
#             else:
#                 print("Unauthorized message received:", payload)
#         except Exception as e:
#             print(f"Error consuming message: {e}")

# async def start_consumer():
#     try:
#         connection = await connect_robust("amqp://guest:guest@localhost/")
#         async with connection.channel() as channel:
#             queue = await channel.declare_queue("security_monitor_queue", durable=True)
#             await queue.consume(consume)
#     except Exception as e:
#         print(f"Error starting consumer: {e}")

# if __name__ == "__main__":
#     get_event_loop().run_until_complete(start_consumer())

import pika
import json
import base64
from policies import check_operation, check_payload_seal

HOST = '127.0.0.1'
QUEUE_NAME = 'security_monitor_queue'

def on_message(ch, method, properties, body):
    message = json.loads(body.decode())
    message_id = message.get('id')
    details = message.get('details')

    if check_operation(message_id, details):
        print(f'[info] Message {message_id} is authorized')
        routing_key = details['deliver_to']
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
    
