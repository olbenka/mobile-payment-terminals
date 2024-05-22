# #control_imput/producer.py
# import aio_pika

# async def consume_keyboard_input(connection):
#     async with connection:
#         channel = await connection.channel()

#         queue_name = "keyboard_input_queue"
#         queue = await channel.declare_queue(queue_name, auto_delete=True)

#         async with queue.iterator() as queue_iter:
#             async for message in queue_iter:
#                 async with message.process():
#                     print("Control Input received:", message.body.decode())



# async def consume_keyboard_input(connection):
#     async with connection:
#         channel = await connection.channel()

#         keyboard_input_queue = await channel.declare_queue("keyboard_input_queue", auto_delete=True)

#         async with aio_pika.QueueConsumption(channel, keyboard_input_queue) as queue_consumption:
#             async for message in queue_consumption:
#                 async with message.process():
#                     print("Control Input received keyboard input:", message.body.decode())

# async def consume_battery_status(connection):
#     async with connection:
#         channel = await connection.channel()

#         battery_status_queue = await channel.declare_queue("battery_to_control", auto_delete=True)

#         async with aio_pika.QueueConsumption(channel, battery_status_queue) as queue_consumption:
#             async for message in queue_consumption:
#                 async with message.process():
#                     print("Control Input received battery status:", message.body.decode())

# async def consume_card_reader(connection):
#     async with connection:
#         channel = await connection.channel()

#         battery_status_queue = await channel.declare_queue("card_messages", auto_delete=True)

#         async with aio_pika.QueueConsumption(channel, battery_status_queue) as queue_consumption:
#             async for message in queue_consumption:
#                 async with message.process():
#                     print("Control Input received card-reader data:", message.body.decode())

# async def consume_nfc(connection):
#     async with connection:
#         channel = await connection.channel()

#         battery_status_queue = await channel.declare_queue("nfc_messages", auto_delete=True)

#         async with aio_pika.QueueConsumption(channel, battery_status_queue) as queue_consumption:
#             async for message in queue_consumption:
#                 async with message.process():
#                     print("Control Input received nfc data:", message.body.decode())

# import aio_pika

import pika
import json
from producer import send_message

HOST = '127.0.0.1'
QUEUE_NAME = 'control_input_queue'

def on_message(ch, method, properties, body):
    message = json.loads(body.decode())
    message_id = message.get('id')
    details = message.get('details')

    print(f'[info] Control Input received message {message_id}: {details}')

    # Отправляем сообщение в central
    message = {
        'id': 'control_input_data',
        'details': {
            'source': 'control_input',
            'deliver_to': 'central',
            'operation': 'send_keyboard_input',
            'amount': details.get('amount')
        }
    }
    send_message('central_queue', message)

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(HOST))
    channel = connection.channel()

    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=on_message, auto_ack=True)

    print('Control Input is listening...')
    channel.start_consuming()

if __name__ == '__main__':
    main()