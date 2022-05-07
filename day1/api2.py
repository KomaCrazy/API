from flask import Flask
from yaml.loader import SafeLoader,FullLoader
import yaml
host = "0.0.0.0"
port = 5000 

app = Flask(__name__)

@app.route('/')
def main():
    return 'test'

@app.route('/1')
def on1():
    data = open("config.yaml",'r')
    data = yaml.load(data,Loader=FullLoader)
    data = data["box1"]["cmd"]
    return data

@app.route('/up')
def on2():
    


if __name__ == '__main__':
    app.run(host,port)