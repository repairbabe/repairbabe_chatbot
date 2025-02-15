import flask
from flask import request, jsonify
import requests

app = flask.Flask(__name__)
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Repair Babe Chatbot API is running!"

@app.route("/chat", methods=["GET"])
def chat():
    user_message = request.args.get("message", "").lower()
    responses = {
        "hello": "Hi there! How can I assist you today?",
        "pricing": "I can help with pricing. What device do you need repaired?",
        "bye": "Goodbye! Let me know if you need anything else!"
    }
    bot_response = responses.get(user_message, "I'm not sure I understand, but I'm here to help!")
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

# Function to fetch part prices from Amazon
def get_amazon_price(part_name):
    search_url = f"https://www.amazon.com/s?k={part_name.replace(' ', '+')}"
    return f"Check price here: {search_url}"

# Repair pricing structure
LABOR_COSTS = {
    "Cell phone": 80.00,
    "Laptop / Computer": 150.00,
    "Tablet": 75.00,
    "Gaming Console": 75.00,
    "Smart Watch": 75.00,
    "Remote controls": 35.00,
    "iPod": 40.00,
    "Device Unlock": 45.00,
    "Battery": 75.00,
    "Headphone": 40.00
}
TRANSACTION_FEE = 35.00

@app.route('/get_quote', methods=['POST'])
def get_quote():
    data = request.json
    device_type = data.get("device_type")
    part_name = data.get("part_name")

    if device_type not in LABOR_COSTS:
        return jsonify({"error": "Invalid device type"}), 400

    amazon_price_link = get_amazon_price(part_name)
    total_cost = LABOR_COSTS[device_type] + TRANSACTION_FEE

    return jsonify({
        "message": f"Repair Quote for {device_type} ({part_name}):\nLabor: ${LABOR_COSTS[device_type]:.2f}\nFee: ${TRANSACTION_FEE:.2f}\n{amazon_price_link}"
    })

@app.route('/')
def home():
    return "Repair Babe Chatbot API is running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
