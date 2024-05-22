from flask import Flask, jsonify
from producer import send_message

app = Flask(__name__)

# @app.route('/transaction_status', methods=['GET'])
# def get_transaction_status():
#     # Отправка запроса на статус транзакции
#     message = {
#         'id': 'get_transaction_status',
#         'details': {
#             'source': 'screen',
#             'deliver_to': 'central',
#             'operation': 'get_transaction_status'
#         }
#     }
#     send_message('central_queue', message)

#     return jsonify({'status': 'success', 'message': 'Транзакция одобрена'})

if __name__ == '__main__':
    app.run(debug=True, port=6004, host="0.0.0.0")