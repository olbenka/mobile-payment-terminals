import asyncio
import aio_pika

#тут мы отправляем данные из nfc в контроль ввода
async def send_message(message, routing_key):
    connection = await aio_pika.connect_robust(
        "amqp://guest:guest@127.0.0.1/",
    )

    async with connection:
        channel = await connection.channel()

        await channel.default_exchange.publish(
            aio_pika.Message(body=message.encode()),
            routing_key=routing_key,
        )
        print(f"Message sent: {message}")

async def main():
    message = "Hello from nfc producer!"
    routing_key = "nfc_messages"
    await send_message(message, routing_key)

if __name__ == "__main__":
    asyncio.run(main())