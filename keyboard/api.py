import asyncio
import aio_pika
from .producer import send_keyboard_input

async def main():
    connection = await aio_pika.connect_robust(
        "amqp://guest:guest@127.0.0.1/",
    )
    await send_keyboard_input(connection)

if __name__ == "__main__":
    asyncio.run(main())
