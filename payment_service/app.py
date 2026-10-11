from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/pay", methods=["GET"])
def pay():
    return jsonify({
        "payment_status": "SUCCESS",
        "message": "Payment simulated successfully"
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5002)
