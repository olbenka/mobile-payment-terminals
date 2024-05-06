import asyncio
import aio_pika
from .producer import send_battery_info

async def main():
    connection = await aio_pika.connect_robust(
        "amqp://guest:guest@127.0.0.1/",
    )
    await send_battery_info(connection)

if __name__ == "__main__":
    asyncio.run(main())
