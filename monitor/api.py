from aio_pika import connect_robust, Message
import asyncio
from json import dumps
from policies import check_operation
# import sys
# sys.path.insert(0, '/home/nadya/PI/mobile-payment-terminals/monitor')



async def send_message(payload):
    try:
        connection = await connect_robust("amqp://guest:guest@localhost/")
        async with connection.channel() as channel:
            exchange = await channel.declare_exchange("microservices_exchange", durable=True)
            routing_key = get_routing_key(payload)
            if routing_key:
                message = Message(body=dumps(payload).encode())
                await exchange.publish(message, routing_key=routing_key)
                print("Message sent successfully.")
            else:
                print("Invalid message format.")
    except Exception as e:
        print(f"Error sending message: {e}")

def get_routing_key(payload):
    src = payload.get('source', '')
    dst = payload.get('destination', '')
    operation = payload.get('operation', '')
    if check_operation(src, dst, operation):
        return f"{src}.{dst}"
    return None
