import pika, sys, os

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

   # Функция обратного вызова, которая будет вызываться при получении сообщения из очереди
    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")


    # Подписываемся на очередь 'hello' и указываем функцию обратного вызова
    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    
     # Запускаем бесконечный цикл ожидания сообщений
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
            
            
            
#РАБОТАЕТ!! ахахах(прикол, если бы нет, ведь это дока)

# windows: rabbitmq-plugins enable rabbitmq_management
        #  rabbitmq-service.bat stop
        #  rabbitmq-service.bat start

# ubuntu:  sudo rabbitmq-plugins enable rabbitmq_management
#          sudo service rabbitmq-server restart
# http://localhost:15672/

# шаги: 1. запускайте в терминале этот файл recieve  
#       2. во втором терминале запускайте sent и смотрите терминал первого, там должно быть так: 
# nadya@DESKTOP-7I28LQI:~/PI/mobile-payment-terminals$ python3 test_rabbit_recieve.py 
#  [*] Waiting for messages. To exit press CTRL+C
#  [x] Received b'Hello World!'
# ^CInterrupted