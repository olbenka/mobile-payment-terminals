# central/producer.py

import asyncio
import aio_pika

async def send_message(message, routing_key):
    connection = await aio_pika.connect_robust(
        "amqp://guest:guest@127.0.0.1/",
    )

    async with connection:
        channel = await connection.channel()

        await channel.default_exchange.publish(
            aio_pika.Message(body=message.encode()),
            routing_key=routing_key,  # Маршрутный ключ для отправки сообщения в центральный сервис
        )
        print(f"Message sent: {message}")

async def main():
    message = "Hello from central producer!"
    routing_key = "central_messages"  # Маршрутный ключ для отправки сообщения в центральный сервис
    await send_message(message, routing_key)

if __name__ == "__main__":
    asyncio.run(main())
