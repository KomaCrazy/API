from flask import Flask 
from flask_cors import CORS 
app = Flask(__name__)
CORS(app)

host = '0.0.0.0'
port = 5000


class server:
    def on():
        app.run(host,port)