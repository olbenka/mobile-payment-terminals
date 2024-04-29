from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/central",methods=['GET'])
def hello_connection():
    message = {"message" : "hi, Albina! It's Nadya fron central"}
    return jsonify(message)

if __name__ == "__main__":
    app.run(port=8001)