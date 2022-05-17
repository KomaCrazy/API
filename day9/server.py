from flask import Flask 
from tools import *
app = Flask(__name__)


@app.route(link0)
def link0():
    return 'hello'

@app.route(link1)
def link1():
    return 'hello'

@app.route(link2)
def link2():
    return 'kaw'

if __name__ == '__main__':
    app.run(host,port)