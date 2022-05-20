from os import rename
from flask import Flask
app = Flask(__name__)

host = '0.0.0.0'
port = 5000

@app.route('/')
def page():
    return '0'

app.run(host,port)

