from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/notify", methods=["GET"])
def notify():
    return jsonify({
        "notification_status": "SENT",
        "message": "Order confirmation simulated"
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5003)

