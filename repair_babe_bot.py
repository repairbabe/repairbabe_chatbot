from flask import Flask, request, jsonify

app = Flask(__name__)

# ✅ Fix: Ensure there's only one home route
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Repair Babe Chatbot API is running!"})

# ✅ Chatbot Route: Processes user input & returns a response
@app.route("/chat", methods=["GET"])
def chat():
    user_message = request.args.get("message", "").lower()

    responses = {
        "hello": "Hi there! How can I assist you today?",
        "pricing": "I can help with pricing. What device do you need repaired?",
        "bye": "Goodbye! Let me know if you need anything else!",
        "repair": "We repair phones, laptops, tablets, and more! What do you need help with?",
    }

    bot_response = responses.get(user_message, "I'm not sure I understand, but I'm here to help!")
    return jsonify({"response": bot_response})

# ✅ Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
