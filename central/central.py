# central/api.py

# import asyncio
# import aio_pika
# from producer import send_message
# from consumer import consume_messages

# async def main():
#     connection = await aio_pika.connect_robust(
#         "amqp://guest:guest@127.0.0.1/",
#     )
#     routing = "central_to_connection"
#     # await send_message("Hello from central producer!", routing)
#     # await asyncio.sleep(10)
#     routing_key = "control_to_central"
#     await consume_messages(connection, routing_key)

# if __name__ == "__main__":
#     asyncio.run(main())


# import asyncio
# import aio_pika
# from producer import send_message

# async def send_message_to_printer():
#     message = "Hello from central producer to printer!"
#     routing_key = "central_to_printer"
#     await send_message(message, routing_key)

# async def send_message_to_screen():
#     message = "Hello from central producer to screen!"
#     routing_key = "central_to_screen"
#     await send_message(message, routing_key)

# async def send_message_to_connection():
#     message = "Hello from central producer to connection!"
#     routing_key = "central_messages"
#     await send_message(message, routing_key)

# async def main():
#     await asyncio.gather(
#         send_message_to_printer(),
#         send_message_to_screen(),
#         send_message_to_connection()
#     )

# if __name__ == "__main__":
#     asyncio.run(main())


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

# @app.route('/start_transaction', methods=['POST'])
# def start_transaction():
#     message = {
#         'id': 'start_transaction',
#         'details': {
#             'source': 'central',
#             'deliver_to': 'screen',
#             'operation': 'start_transaction'
#         }
#     }
#     send_message('security_monitor_queue', message)

#     return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)