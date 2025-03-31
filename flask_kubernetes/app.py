from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    # Get the 'number' query parameter
    number = request.args.get("number", default=None, type=int)
    
    if number is None:
        return jsonify(message="Please provide a 'number' query parameter as an integer."), 400
    print(f"You provided the number: {number}")
    return jsonify(message=f"You provided the number: {number}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
