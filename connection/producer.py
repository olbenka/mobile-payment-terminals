import json
import pika

def func_producer(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    exchange_name = 'connection_name'
    routing_key = 'connection_queue'
    
    channel.exchange_declare(exchange=exchange_name, exchange_type='direct', durable=True)
    channel.basic_publish(exchange=exchange_name, routing_key=routing_key, body=json.dumps(message))
    
    print("work_connection")
    connection.close()
    

