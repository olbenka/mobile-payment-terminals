# import aio_pika

# async def send_to_central(connection):
#     async with connection:
#         channel = await connection.channel()

#         routing_key = "central_messages"
#         await channel.default_exchange.publish(
#             aio_pika.Message(body=b"Data from Control Input"),
#             routing_key=routing_key
#         )
#         print("Data from Control Input sent to Central.")
import aio_pika

async def send_to_central(connection, routing_key1):
    async with connection:
        channel = await connection.channel()

        await channel.default_exchange.publish(
            aio_pika.Message(body=b"Data from Control Input"),
            routing_key=routing_key1
        )
        print("LOCAL_LOG: Data from Control Input sent to Central.")
