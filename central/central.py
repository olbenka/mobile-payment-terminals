
from flask import Flask, request, jsonify
from producer import send_message

app = Flask(__name__)

@app.route('/authorize_purchase', methods=['POST'])
def authorize_purchase():
    data = request.get_json()
    amount = data.get('amount')

    if amount is None or amount <= 0:
        return jsonify({'status': 'error', 'message': 'Invalid amount'}), 400

    message = {
        'id': 'authorize_purchase',
        'details': {
            'source': 'central',
            'deliver_to': 'screen',
            'operation': 'authorize_transaction',
            'amount': amount
        }
    }
    send_message('security_monitor_queue', message)

    return jsonify({'status': 'success'})


if __name__ == '__main__':
    app.run(debug=True, port=6002, host="0.0.0.0")