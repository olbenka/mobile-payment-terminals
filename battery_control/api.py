import asyncio
import aio_pika
from producer import send_battery_info

async def main():
    connection = await aio_pika.connect_robust(
        "amqp://guest:guest@rabbitmq/",
    )
    routing_key = "battery_to_control"
    await send_battery_info(connection, routing_key)

if __name__ == "__main__":
    asyncio.run(main())
