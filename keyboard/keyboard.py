from flask import Flask, request, jsonify
from producer import send_message

app = Flask(__name__)

@app.route('/keyboard_data', methods=['POST'])
def keyboard_data():
    data = request.get_json()
    amount = data.get('amount')

    if amount is None or amount <= 0:
        return jsonify({'status': 'error', 'message': 'Invalid amount'}), 400

    message = {
        'id': 'keyboard_data',
        'details': {
            'source': 'keyboard',
            'deliver_to': 'control_input',
            'operation': 'send_keyboard_input',
            'amount': amount
        }
    }
    try:
        send_message('security_monitor_queue', message)
        print(f'[info] Sent message to security_monitor_queue: {message}')
    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Error sending message: {e}'}), 500

    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True, port=6003, host="0.0.0.0")
