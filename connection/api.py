# # connection/api.py

# import asyncio
# import subprocess
# from producer import send_message
# from consumer import consume_messages

# async def start_consumer():
#     await asyncio.create_subprocess_exec(
#         "python3", "producer.py",
#         cwd="/home/nadya/PI/mobile-payment-terminals/connection/", stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
#     )

# async def start_producer():
#     await asyncio.create_subprocess_exec(
#         "python3", "producer.py",
#         cwd="/home/nadya/PI/mobile-payment-terminals/connection/", stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
#     )

# async def main():
#     await asyncio.gather(start_consumer(), start_producer())

# if __name__ == "__main__":
#     asyncio.run(main())


# # connection/api.py

# import asyncio
# import aio_pika
# from producer import send_message
# from consumer import consume_messages

# async def main():
#     connection = await aio_pika.connect_robust(
#         "amqp://guest:guest@127.0.0.1/",
#     )
#     await consume_messages(connection)
#     # await asyncio.sleep(200)
#     # await send_message("Hello from connection producer!", "connection_to_central")

# if __name__ == "__main__":
#     asyncio.run(main())


import asyncio
import aio_pika
from producer import send_message_secure
from consumer import consume_messages_secure

async def main():
    connection = await aio_pika.connect_robust("amqp://guest:guest@127.0.0.1/")
    await consume_messages_secure(connection)
    await send_message_secure("Hello from connection producer!", "connection_to_central")

if __name__ == "__main__":
    asyncio.run(main())
