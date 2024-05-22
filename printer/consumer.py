import asyncio
import aio_pika

async def consume_messages_printer(connection):
    async with connection:
        channel = await connection.channel()

        queue_name = "central_to_printer"  # Используем тот же маршрутный ключ, что и в центральном сервисе
        queue = await channel.declare_queue(queue_name, auto_delete=True)

        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    print('here!!!')    
                    print("MeSsagE received Nadya:", message.body.decode())

async def main():
    connection = await aio_pika.connect_robust(
        "amqp://guest:guest@rabbitmq/",
    )
    await consume_messages_printer(connection)

if __name__ == "__main__":
    asyncio.run(main())