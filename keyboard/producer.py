import asyncio
import aio_pika

async def send_keyboard_input(connection):
    async with connection:
        channel = await connection.channel()
        message = "Hello from keyboard"

        routing_key1 = "keyboard_to_control"
        await channel.default_exchange.publish(
            aio_pika.Message(body=message.encode()),
            routing_key=routing_key1
        )
        print(f"LOCAL_LOG: Keyboard input sent: {message}")
