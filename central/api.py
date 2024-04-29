from flask import Flask, jsonify
from producer import func_producer

app = Flask(__name__)

@app.route("/central",methods=['POST'])
def central_message():
    message = {"message" : "hi, Albina! It's Nadya fron central"}
    func_producer(message)
    return jsonify(message)

if __name__ == "__main__":
    app.run(port=8001)

    
    
# как запускать:
# 1. запустить producer(?)
# 2. в терминале в папке этой python3 api.py
# в постмане проверяла, все норм возвращает. чтобы проверить:
#  1. выбрать пост запрос и адрес http://localhost:8001/central
#  2. в json написала 
# {
#     "key": "value"
# }, но без этого тоже все работает (проверила)
# и отправить запрос. возвращает 200 и само сообщение (победа)
