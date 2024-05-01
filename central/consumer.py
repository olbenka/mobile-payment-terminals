# # связь
# # source:
# # https://aio-pika.readthedocs.io/en/latest/quick-start.html#simple-consumer

# import asyncio
# import logging

# import aio_pika


# async def main() -> None:
#     logging.basicConfig(level=logging.INFO)
#     connection = await aio_pika.connect_robust(
#         "amqp://guest:guest@127.0.0.1/",
#     )

#     queue_name = "test_queue"
#     confirmation_queue_name = "confirmation_queue"  # Очередь для подтверждений получения сообщений

#     async with connection:
#         channel = await connection.channel()

#         await channel.set_qos(prefetch_count=10)

#         queue = await channel.declare_queue(queue_name, auto_delete=True)
#         confirmation_queue = await channel.declare_queue(
#             confirmation_queue_name, auto_delete=True
#         )

#         async with queue.iterator() as queue_iter:
#             async for message in queue_iter:
#                 async with message.process():
#                     print("Received:", message.body.decode())

#                     # Отправка подтверждения
#                     await channel.default_exchange.publish(
#                         aio_pika.Message(body=b"Hello from connection!!!!"),
#                         routing_key=confirmation_queue_name,
#                     )

#                     if queue.name in message.body.decode():
#                         break


# if __name__ == "__main__":
#     asyncio.run(main())
# central/consumer.py

import asyncio
import aio_pika

async def consume_messages(connection):
    async with connection:
        channel = await connection.channel()

        queue_name = "connection_messages"  # Имя очереди, на которую подписывается центральный сервис
        queue = await channel.declare_queue(queue_name, auto_delete=True)

        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    print("Central received:", message.body.decode())

async def main():
    connection = await aio_pika.connect_robust(
        "amqp://guest:guest@127.0.0.1/",
    )
    await consume_messages(connection)

if __name__ == "__main__":
    asyncio.run(main())
