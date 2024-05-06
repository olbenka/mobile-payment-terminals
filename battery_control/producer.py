# battery_status_producer.py
import asyncio
import aio_pika

async def send_battery_info(connection):
    async with connection:
        channel = await connection.channel()

        routing_key = "battery_info_queue"
        await channel.default_exchange.publish(
            aio_pika.Message(body=b"battery info data"),
            routing_key=routing_key
        )
        print("battery info sent.")
