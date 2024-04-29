import pika

# Подключение к RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Определение очередей
channel.queue_declare(queue='from_connection_to_central')
channel.queue_declare(queue='from_central_to_connection')

# Отправка сообщения от connection к central
channel.basic_publish(exchange='', routing_key='from_connection_to_central', body='Hello from connection!')

# Функция для обработки сообщений от central
def callback(ch, method, properties, body):
    print("Received message from central:", body.decode())
    # Отправка ответного сообщения от central к connection
    ch.basic_publish(exchange='', routing_key='from_central_to_connection', body='Hello from central!')

# Прослушивание очереди сообщений от central
channel.basic_consume(queue='from_central_to_connection', on_message_callback=callback, auto_ack=True)

print('Waiting for messages...')
channel.start_consuming()

# # НЕ РАБОТАЕТ
# import pika
# import threading

# # Подключение к RabbitMQ
# connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# channel = connection.channel()

# # Определение очередей
# channel.queue_declare(queue='from_central_to_connection')
# channel.queue_declare(queue='from_connection_to_central')

# # Блокировка для синхронизации отправки сообщений
# lock = threading.Lock()

# # Функция отправки сообщения от central к connection
# def send_message_to_connection():
#     with lock:
#         channel.basic_publish(exchange='', routing_key='from_central_to_connection', body='Hello from central!')

# # Функция для обработки сообщений от connection
# def callback(ch, method, properties, body):
#     print("Received message from connection:", body.decode())
#     # Отправка ответного сообщения от central к connection
#     send_message_to_connection()

# # Прослушивание очереди сообщений от connection
# channel.basic_consume(queue='from_connection_to_central', on_message_callback=callback, auto_ack=True)

# print('Waiting for messages from connection...')
# channel.start_consuming()
