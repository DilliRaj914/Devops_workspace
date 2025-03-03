from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        return jsonify({"result": a + b})
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input"}), 400

@app.route('/subtract', methods=['GET'])
def subtract():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        return jsonify({"result": a - b})
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input"}), 400

if __name__ == '__main__':
    app.run(debug=True)
