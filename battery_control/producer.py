# battery_status_producer.py
import asyncio
import aio_pika

async def send_battery_info(connection, routing_key1):
    async with connection:
        channel = await connection.channel()

        # routing_key = "battery_info_queue"
        await channel.default_exchange.publish(
            aio_pika.Message(body=b"Hello from battery"),
            routing_key=routing_key1,)
            
        print("LOCAL_LOG:battery info sent.")
