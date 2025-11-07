from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def root():
    return jsonify(message="Hello from GKE via GitOps!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

# Test commit to trigger Cloud Build pipeline
Trigger CI pipeline test
