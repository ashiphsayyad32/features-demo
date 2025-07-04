from flask import Flask

app = Flask(__name__)

@app.roe('/')
def home():
    return 'Hello, Cursor Bug Bot!'

hello()



if __name__ == '__main__':
    app.run(debug=True) 