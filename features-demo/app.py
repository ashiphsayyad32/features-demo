from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Cursor Bug Bot!'

@app.route('/bug')
def bug():
    # Intentional bug for demo
    return str(1 / 0)

@app.route('/keyerror')
def keyerror():
    d = {'a': 1}
    return str(d['b'])  # Intentional KeyError

if __name__ == '__main__':
    app.run(debug=True) 