from flask import Flask, jsonify, render_template_string
import requests

app = Flask(__name__)

PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>SOA Shopping Demo</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f6fb;
            text-align: center;
            padding: 50px 15px;
        }
        .card {
            background: white;
            max-width: 500px;
            margin: auto;
            padding: 30px;
            border-radius: 18px;
            box-shadow: 0 8px 25px #0001;
        }
        button {
            background: #5b5bd6;
            color: white;
            border: 0;
            padding: 14px 24px;
            border-radius: 9px;
            cursor: pointer;
            font-size: 16px;
        }
        pre {
            text-align: left;
            white-space: pre-wrap;
            overflow-wrap: anywhere;
            background: #f1f2f8;
            padding: 15px;
            border-radius: 8px;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>SOA Shopping</h1>
        <p>A simple service-oriented shopping simulation</p>
        <h2>Everyday Essentials</h2>
        <p>Demo product · ₹499</p>
        <button onclick="placeOrder()">Place Demo Order</button>
        <div id="result"></div>
    </div>
    <script>
        async function placeOrder() {
            const result = document.getElementById("result");
            result.innerHTML = "<p>Processing order...</p>";
            try {
                const response = await fetch("/order");
                const data = await response.json();
                result.innerHTML = "<h3>Order Result</h3><pre>" +
                    JSON.stringify(data, null, 2) + "</pre>";
            } catch (error) {
                result.innerHTML = "<p>Request failed. Please try again.</p>";
            }
        }
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(PAGE)

@app.route("/order")
def create_order():
    try:
        payment_response = requests.get(
            "http://127.0.0.1:5002/pay", timeout=5
        )
        payment_response.raise_for_status()

        notification_response = requests.get(
            "http://127.0.0.1:5003/notify", timeout=5
        )
        notification_response.raise_for_status()

        return jsonify({
            "order_status": "CREATED",
            "payment": payment_response.json(),
            "notification": notification_response.json()
        })
    except requests.RequestException:
        return jsonify({
            "order_status": "FAILED",
            "message": "A dependent service is unavailable"
        }), 503

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001)
