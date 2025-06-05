from flask import Flask, request, jsonify

app = Flask(__name__)

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

@app.route('/')
def home():
    return 'Welcome to the Prime Checker API! Use /is-prime?number=YOUR_NUMBER'

@app.route('/is-prime', methods=['GET'])
def check_prime():
    try:
        num = int(request.args.get('number'))
    except (TypeError, ValueError):
        return jsonify({'error': 'Please provide a valid integer as "number" parameter.'}), 400

    result = is_prime(num)
    return jsonify({'number': num, 'is_prime': result})

if __name__ == '__main__':
    app.run(debug=True)
