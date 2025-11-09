from flask import Flask, request, jsonify
import os
import socket

app = Flask(__name__)

# message that we can change to trigger CI/CD
DEFAULT_MESSAGE = "Hello from Cloud Build CI/CD GitOps!"

@app.route("/")
def root():
    message = os.getenv("APP_MESSAGE", DEFAULT_MESSAGE)
    return jsonify(
        message=message,
        version=os.getenv("APP_VERSION", "1.0"),
        pod=socket.gethostname()
    )

@app.route("/upper")
def upper():
    text = request.args.get("text", "no text")
    return jsonify(
        original=text,
        upper=text.upper()
    )

@app.route("/reverse")
def reverse():
    text = request.args.get("text", "no text")
    return jsonify(
        original=text,
        reversed=text[::-1]
    )

@app.route("/info")
def info():
    return jsonify(
        pod=socket.gethostname(),
        namespace=os.getenv("POD_NAMESPACE", "default"),
        message_env=os.getenv("APP_MESSAGE", DEFAULT_MESSAGE)
    )

@app.route("/ping")
def ping():
    return "pong", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
