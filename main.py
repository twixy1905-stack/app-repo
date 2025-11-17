from flask import Flask, request, jsonify
import os
import socket
import datetime
import uuid

app = Flask(__name__)

# Konfiguracja i wartości domyślne
DEFAULT_MESSAGE = "Hi from Cloud Build CI/CD GitOps!"
DEFAULT_VERSION = "1.0"
START_TIME = datetime.datetime.utcnow()

def now_iso():
    return datetime.datetime.utcnow().isoformat() + "Z"

@app.route("/")
def root():
    """Główny endpoint: dynamiczny JSON z informacją o wersji, POD-zie i czasie."""
    message = os.getenv("APP_MESSAGE", DEFAULT_MESSAGE)
    version = os.getenv("APP_VERSION", DEFAULT_VERSION)

    return jsonify(
        message=message,
        version=version,
        pod=socket.gethostname(),
        timestamp=now_iso(),
        request_id=str(uuid.uuid4()),
        path=request.path
    )

@app.route("/upper")
def upper():
    """Zwraca tekst UPPERCASE. Przykład: /upper?text=devops"""
    text = request.args.get("text", "no text")
    return jsonify(
        original=text,
        upper=text.upper(),
        timestamp=now_iso()
    )

@app.route("/reverse")
def reverse():
    """Odwraca tekst. Przykład: /reverse?text=cloudbuild"""
    text = request.args.get("text", "no text")
    return jsonify(
        original=text,
        reversed=text[::-1],
        timestamp=now_iso()
    )

@app.route("/echo")
def echo():
    """Prosty echo-endpoint — zwraca to, co wyślesz w ?q= ..."""
    q = request.args.get("q", "")
    return jsonify(
        echo=q,
        length=len(q),
        timestamp=now_iso()
    )

@app.route("/info")
def info():
    """Informacje runtime o POD-zie i konfiguracji z ENV."""
    return jsonify(
        pod=socket.gethostname(),
        namespace=os.getenv("POD_NAMESPACE", "default"),
        message_env=os.getenv("APP_MESSAGE", DEFAULT_MESSAGE),
        version=os.getenv("APP_VERSION", DEFAULT_VERSION),
        timestamp=now_iso()
    )

@app.route("/health")
def health():
    """Endpoint zdrowotny (liveness/readiness)."""
    uptime = (datetime.datetime.utcnow() - START_TIME).total_seconds()
    return jsonify(
        status="ok",
        uptime_seconds=int(uptime),
        pod=socket.gethostname(),
        timestamp=now_iso()
    ), 200

@app.route("/ping")
def ping():
    return "pong", 200

if __name__ == "__main__":
    # Flask w kontenerze (port 8080, 0.0.0.0 aby nasłuchiwać na interfejsie kontenera)
    app.run(host="0.0.0.0", port=8080)
