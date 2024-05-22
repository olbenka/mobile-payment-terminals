import aio_pika
import asyncio
# тут мы должны получить данные из некоторого входа для карты (из virtual_card_data)
async def consume_card_input(connection):
    async with connection:
        channel = await connection.channel()

        queue_name = "card_queue" # прием данных из вне!! из virtual_card_data
        queue = await channel.declare_queue(queue_name, auto_delete=True)

        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    print("Card-reader received data from Input:", message.body.decode())

async def main():
    connection = await aio_pika.connect_robust(
        "amqp://guest:guest@rabbitmq/",
    )
    await consume_card_input(connection)

if __name__ == "__main__":
    asyncio.run(main())