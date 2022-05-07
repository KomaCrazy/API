from flask import Flask
app = Flask(__name__)
host = "0.0.0.0"
port = 5000


@app.route('/')
def page():
    return '0'

@app.route('/1')
def page1():
    return '1'

@app.route('2')
def 

if __name__ == '__main__':
    app.run(host,port)