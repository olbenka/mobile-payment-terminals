# вот документация, я на ubuntu ставила 
# https://www.rabbitmq.com/docs/install-debian#apt-quick-start-cloudsmith
# чтобы проверить установлен ли запустите это sudo service rabbitmq-server status (убунта)
# rabbitmq-service status это на винде

#  pip install pika --upgrade  - это либа для rabbitMQ на питоне
import pika

# это соединение устанавливаем, в доке написано, что вместо локалки можем чисто айпи адрес или имя машины(?)
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Объявляем очередь с именем 'hello', если ее нет
channel.queue_declare(queue='hello')

# Отправляем сообщение в очередь 'hello'
channel.basic_publish(exchange='', # тут сообщение никогда не может быть отправлено напрямую в очередь, 
                                    #оно всегда должно проходить через exchange
                      routing_key='hello', #Этот exchange особенный - он позволяет нам точно указать, в какую очередь должно пойти сообщение. 
                                            #Имя очереди должно быть указано в параметре routing_key
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")

connection.close()



