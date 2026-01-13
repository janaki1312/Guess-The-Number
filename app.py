from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

secret_number = random.randint(1, 100)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/guess", methods=["POST"])
def guess():
    global secret_number

    user_guess = int(request.json["guess"])
    max_range = int(request.json["max"])

    if user_guess > secret_number:
        return jsonify({"result": "Too high! 🔼"})
    elif user_guess < secret_number:
        return jsonify({"result": "Too low! 🔽"})
    else:
        secret_number = random.randint(1, max_range)
        return jsonify({"result": "Correct! 🎉 New number generated 💗"})

@app.route("/reset", methods=["POST"])
def reset():
    global secret_number
    max_range = int(request.json["max"])
    secret_number = random.randint(1, max_range)
    return jsonify({"status": "reset"})



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

