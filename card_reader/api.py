import asyncio
import aio_pika
from .producer import send_message
from .consumer import consume_card_input

async def main():
    connection = await aio_pika.connect_robust(
        "amqp://guest:guest@rabbitmq/",
    )
    await send_message("Hello from card reader producer!", "card_messages") #отправка в контроль
    await asyncio.sleep(10)
    #await consume_card_input(connection)

if __name__ == "__main__":
    asyncio.run(main())