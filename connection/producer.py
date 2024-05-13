# connection/producer.py

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
#     message = "Hello from connection producer!"
#     routing_key = "connection_messages"
#     await send_message(message, routing_key)

# if __name__ == "__main__":
#     asyncio.run(main())

import aio_pika
from ..monitor.api import send_message

async def send_message_secure(message, routing_key):
    payload = {
        "source": "connection",
        "destination": routing_key.split("_")[0],
        "operation": "send_message",
        "message": message
    }
    await send_message(payload, "security_monitor")

