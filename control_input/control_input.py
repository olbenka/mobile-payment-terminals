from flask import Flask, request, jsonify
from producer import send_message

app = Flask(__name__)

@app.route('/input_data', methods=['POST'])
def input_data():
    data = request.get_json()
    amount = data.get('amount')

    if amount is None or amount <= 0:
        return jsonify({'status': 'error', 'message': 'Invalid amount'}), 400

    message = {
        'id': 'input_data',
        'details': {
            'source': 'control_input',
            'deliver_to': 'central',
            'operation': 'send_keyboard_input',
            'amount': amount
        }
    }
    send_message('security_monitor_queue', message)
    print(f'[info] Sent message to security_monitor_queue: {message}')

    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True, port=6000, host="0.0.0.0")
