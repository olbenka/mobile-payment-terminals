import asyncio
import aio_pika

async def send_keyboard_input(connection):
    async with connection:
        channel = await connection.channel()

        routing_key = "keyboard_input_queue"
        await channel.default_exchange.publish(
            aio_pika.Message(body=b"Keyboard input data"),
            routing_key=routing_key
        )
        print("Keyboard input sent.")
