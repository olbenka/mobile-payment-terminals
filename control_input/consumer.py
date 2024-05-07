# #control_imput/producer.py
# import aio_pika

# async def consume_keyboard_input(connection):
#     async with connection:
#         channel = await connection.channel()

#         queue_name = "keyboard_input_queue"
#         queue = await channel.declare_queue(queue_name, auto_delete=True)

#         async with queue.iterator() as queue_iter:
#             async for message in queue_iter:
#                 async with message.process():
#                     print("Control Input received:", message.body.decode())



# async def consume_keyboard_input(connection):
#     async with connection:
#         channel = await connection.channel()

#         keyboard_input_queue = await channel.declare_queue("keyboard_input_queue", auto_delete=True)

#         async with aio_pika.QueueConsumption(channel, keyboard_input_queue) as queue_consumption:
#             async for message in queue_consumption:
#                 async with message.process():
#                     print("Control Input received keyboard input:", message.body.decode())

# async def consume_battery_status(connection):
#     async with connection:
#         channel = await connection.channel()

#         battery_status_queue = await channel.declare_queue("battery_to_control", auto_delete=True)

#         async with aio_pika.QueueConsumption(channel, battery_status_queue) as queue_consumption:
#             async for message in queue_consumption:
#                 async with message.process():
#                     print("Control Input received battery status:", message.body.decode())

# async def consume_card_reader(connection):
#     async with connection:
#         channel = await connection.channel()

#         battery_status_queue = await channel.declare_queue("card_messages", auto_delete=True)

#         async with aio_pika.QueueConsumption(channel, battery_status_queue) as queue_consumption:
#             async for message in queue_consumption:
#                 async with message.process():
#                     print("Control Input received card-reader data:", message.body.decode())

# async def consume_nfc(connection):
#     async with connection:
#         channel = await connection.channel()

#         battery_status_queue = await channel.declare_queue("nfc_messages", auto_delete=True)

#         async with aio_pika.QueueConsumption(channel, battery_status_queue) as queue_consumption:
#             async for message in queue_consumption:
#                 async with message.process():
#                     print("Control Input received nfc data:", message.body.decode())

# import aio_pika


async def consume_messages(connection, routing_key1):
    async with connection:
        channel = await connection.channel()
        queue_name = routing_key1  
        queue = await channel.declare_queue(queue_name, auto_delete=True)
        async with queue.iterator() as queue_iter:
            # print(queue_iter)
            async for message in queue_iter:
                # print('here')
                async with message.process():
                    print("Control received:", message.body.decode())