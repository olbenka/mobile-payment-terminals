# connection/consumer.py

import asyncio
import aio_pika

async def consume_messages(connection):
    async with connection:
        channel = await connection.channel()

        queue_name = "central_messages"  # Используем тот же маршрутный ключ, что и в центральном сервисе
        queue = await channel.declare_queue(queue_name, auto_delete=True)

        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    print("Connection received:", message.body.decode())

async def main():
    connection = await aio_pika.connect_robust(
        "amqp://guest:guest@127.0.0.1/",
    )
    await consume_messages(connection)

if __name__ == "__main__":
    asyncio.run(main())
