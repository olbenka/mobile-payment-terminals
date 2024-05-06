# control_input/api.py

import asyncio
import aio_pika
from .consumer import consume_keyboard_input, consume_battery_status
from .producer import send_to_central

async def main():
    connection = await aio_pika.connect_robust(
        "amqp://guest:guest@127.0.0.1/",
    )
    await asyncio.gather(
        #consume_keyboard_input(connection), 
        consume_battery_status(connection),
        send_to_central(connection)
    )

if __name__ == "__main__":
    asyncio.run(main())