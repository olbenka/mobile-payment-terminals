import asyncio
import aio_pika
from consumer import consume_messages_printer

async def main():
    connection = await aio_pika.connect_robust(
        "amqp://guest:guest@rabbitmq/",
    )
    await consume_messages_printer(connection)
    # await asyncio.sleep(200)
    

if __name__ == "__main__":
    asyncio.run(main())
