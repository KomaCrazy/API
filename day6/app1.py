from flask import Flask

app = Flask(__name__)

host = '0.0.0.0'
port = 5000

link1 = "/1"
data1 = '1'

@app.route("/")
def page():
    return '0'

@app.route(link1)
def page1():
    return data1

if __name__ == '__main__':
    app.run(host,port)