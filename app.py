from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Addition Service\n'

@app.route('/add')
def add():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        result = num1 + num2
        return f'The sum of {num1} and {num2} is {result}\n'
    except:
        return 'Invalid input. Please provide valid numbers.\n'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)