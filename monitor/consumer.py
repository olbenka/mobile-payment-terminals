from aio_pika import connect_robust, IncomingMessage
from asyncio import get_event_loop
from json import loads
from policies import check_operation

async def consume(message: IncomingMessage):
    async with message.process():
        try:
            payload = loads(message.body.decode())
            src = payload.get('source', '')
            dst = payload.get('destination', '')
            operation = payload.get('operation', '')
            if check_operation(src, dst, operation):
                print("Authorized message received:", payload)
            else:
                print("Unauthorized message received:", payload)
        except Exception as e:
            print(f"Error consuming message: {e}")

async def start_consumer():
    try:
        connection = await connect_robust("amqp://guest:guest@localhost/")
        async with connection.channel() as channel:
            queue = await channel.declare_queue("security_monitor_queue", durable=True)
            await queue.consume(consume)
    except Exception as e:
        print(f"Error starting consumer: {e}")

if __name__ == "__main__":
    get_event_loop().run_until_complete(start_consumer())
