import asyncio
import aio_pika
from .producer import send_message
from .consumer import consume_nfc_input

async def main():
    connection = await aio_pika.connect_robust(
        "amqp://guest:guest@127.0.0.1/",
    )
    await send_message("Hello from nfc producer!", "nfc_messages") #отправка в контроль
    await asyncio.sleep(10)
    #await consume_nfc_input(connection)

if __name__ == "__main__":
    asyncio.run(main())