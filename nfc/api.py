import asyncio
import aio_pika
from producer import send_message
from consumer import consume_nfc_input

async def main():
    connection = await aio_pika.connect_robust(
        "amqp://guest:guest@127.0.0.1/",
    )
    routing_key = "nfc_to_control"
    await send_message("Hello from nfc producer!", routing_key) #отправка в контроль
    await asyncio.sleep(10)
    #await consume_nfc_input(connection)

if __name__ == "__main__":
    asyncio.run(main())