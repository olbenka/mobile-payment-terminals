# # connection/producer.py

# import asyncio
# import aio_pika

# async def consume_messages(connection):
#     async with connection:
#         channel = await connection.channel()

#         queue_name = "central_to_connection"  # Используем тот же маршрутный ключ, что и в центральном сервисе
#         queue = await channel.declare_queue(queue_name, auto_delete=True)

#         async with queue.iterator() as queue_iter:
#             async for message in queue_iter:
#                 async with message.process():
#                     print("Connection received:", message.body.decode())

# async def main():
#     connection = await aio_pika.connect_robust(
#         "amqp://guest:guest@127.0.0.1/",
#     )
#     await consume_messages(connection)

# if __name__ == "__main__":
#     asyncio.run(main())


import aio_pika
from ..monitor.policies import check_operation
from ..monitor.api import send_message
from json import loads

async def consume_messages_secure(connection):
    async with connection:
        channel = await connection.channel()

        queue_name = "security_monitor_queue"
        queue = await channel.declare_queue(queue_name, auto_delete=True)

        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    payload = loads(message.body.decode())
                    if check_operation(payload['source'], payload['destination'], payload['operation']):
                        print("Authorized message received:", payload)
                        await send_message(payload, f"{payload['source']}_to_{payload['destination']}")
                    else:
                        print("Unauthorized message received:", payload)
