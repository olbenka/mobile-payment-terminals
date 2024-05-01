# publisher
import asyncio
import logging

import aio_pika


async def main() -> None:
    logging.basicConfig(level=logging.INFO)
    connection = await aio_pika.connect_robust(
        "amqp://guest:guest@127.0.0.1/",
    )

    queue_name = "test_queue"
    confirmation_queue_name = "confirmation_queue"

    async with connection:
        routing_key = queue_name

        channel = await connection.channel()

        await channel.default_exchange.publish(
            aio_pika.Message(body=f"Hello {routing_key}".encode()),
            routing_key=routing_key,
        )

        # Ожидание подтверждения от потребителя
        confirmation_queue = await channel.declare_queue(
            confirmation_queue_name, auto_delete=True
        )
        async with confirmation_queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    print("Response in central:", message.body.decode())
                    break


if __name__ == "__main__":
    asyncio.run(main())
