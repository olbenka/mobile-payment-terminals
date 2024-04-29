from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/hello",methods=['GET'])
def hello_connection():
    message = {"message" : "hello from connection microservice!"}
    return jsonify(message)

if __name__ == "__main__":
    app.run(port=8000)