from flask import Flask, request, jsonify
import json
import redis

app = Flask(__name__)

REDIS_HOST = 'redis'
r = redis.Redis(host=REDIS_HOST, port=6379, db=0)

@app.route('/last_transaction', methods=['GET'])
def last_transaction():
    messages = r.lrange('messages', 0, -1)
    print(f'[info] Current messages in last_transaction: {messages}')
    if not messages:
        return jsonify({'status': 'error', 'message': 'No transactions available'}), 404
    return jsonify(json.loads(messages[-1]))

if __name__ == '__main__':
    app.run(debug=True, port=6004, host="0.0.0.0")
