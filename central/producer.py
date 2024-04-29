import json
import pika

def func_producer(message):
    connection = pika.BlockingConnection()
    channel = connection.channel()

    exchange_name = 'central_name'
    routing_key = 'central_queue'

    channel.exchange_declare(exchange=exchange_name, exchange_type='topic', durable=True)

    message_json = json.dumps(message)
    
    channel.basic_publish(exchange=exchange_name, routing_key=routing_key, body=message_json)
    
    print("work_central")
    connection.close()
    

