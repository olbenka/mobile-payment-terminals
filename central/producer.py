# # central/producer.py

# import asyncio
# import aio_pika

# async def send_message(message, routing_key):
#     connection = await aio_pika.connect_robust(
#         "amqp://guest:guest@127.0.0.1/",
#     )
#     # print(routing_key)

#     async with connection:
#         channel = await connection.channel()

#         await channel.default_exchange.publish(
#             aio_pika.Message(body=message.encode()),
#             routing_key=routing_key,  # Маршрутный ключ для отправки сообщения в центральный сервис
#         )
#         print(f"Message sent: {message}")

# async def main():
#     message = "Hello from central producer111!"
#     print(routing_key)
#     routing_key = "central_to_printer"  # Маршрутный ключ для отправки сообщения в центральный сервис
#     await send_message(message, routing_key)

# if __name__ == "__main__":
#     asyncio.run(main())



# import asyncio
# import aio_pika

# async def send_message(message, routing_key):
#     connection = await aio_pika.connect_robust(
#         "amqp://guest:guest@127.0.0.1/",
#     )

#     async with connection:
#         channel = await connection.channel()

#         await channel.default_exchange.publish(
#             aio_pika.Message(body=message.encode()),
#             routing_key=routing_key,
#         )
#         print(f"Message sent: {message}")

# async def main():
#     message_to_printer = "Hello from central producer to printer!"
#     routing_key_to_printer = "central_to_printer"
#     await send_message(message_to_printer, routing_key_to_printer)

#     message_to_screen = "Hello from central producer to screen!"
#     routing_key_to_screen = "central_to_screen"
#     await send_message(message_to_screen, routing_key_to_screen)

#     message_to_connection = "Hello from central producer to connection!"
#     routing_key_to_connection = "central_messages"
#     await send_message(message_to_connection, routing_key_to_connection)

# if __name__ == "__main__":
#     asyncio.run(main())





# from monitor.api import send_message


# async def send_message_secure(message, routing_key):
#     payload = {
#         "source": "central",
#         "destination": routing_key.split("_")[0],
#         "operation": "send_message",
#         "message": message
#     }
#     await send_message(payload, "security_monitor")

import pika
import json

HOST = '127.0.0.1'

def send_message(routing_key, message):
    connection = pika.BlockingConnection(pika.ConnectionParameters(HOST))
    channel = connection.channel()

    # Отправка сообщения в очередь микросервиса
    channel.basic_publish(exchange='', routing_key=routing_key, body=json.dumps(message))

    connection.close()