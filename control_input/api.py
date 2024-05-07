# control_input/api.py

import asyncio
import aio_pika
from consumer import consume_messages
from producer import send_to_central

# async def monitor_reciever(connection, routing_key):
#     await consume_messages(connection, routing_key)

async def main():
    connection = await aio_pika.connect_robust(
        "amqp://guest:guest@127.0.0.1/",
    )
    routing_key_bat = "battery_to_control"
    # await consume_messages(connection,routing_key_bat)
    routing_key_keyb = "keyboard_to_control"
    # await consume_messages(connection,routing_key_keyb)
    routing_key_nfc = "nfc_to_control"
    # await consume_messages(connection,routing_key_nfc)
    
   
        #consume_keyboard_input(connection),
    # await consume_messages(connection)
        # consume_card_reader(connection),
        #consume_nfc(connection),
    routing_key_central = "control_to_central"
    send_to_central(connection, routing_key_central)
    

if __name__ == "__main__":
    asyncio.run(main())