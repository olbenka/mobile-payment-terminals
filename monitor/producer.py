from aio_pika import connect_robust, Message
from asyncio import get_event_loop
from json import dumps

async def produce():
    try:
        connection = await connect_robust("amqp://guest:guest@localhost/")
        async with connection.channel() as channel:
            queue = await channel.declare_queue("security_monitor_queue", durable=True)
            message = {"source": "central", "destination": "printer", "operation": "print_document", "payload": "Base64EncodedPayload"}
            await queue.publish(Message(body=dumps(message).encode()))
            print("Message produced successfully.")
    except Exception as e:
        print(f"Error producing message: {e}")

if __name__ == "__main__":
    get_event_loop().run_until_complete(produce())
