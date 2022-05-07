from flask import Flask
import yaml
from yaml.loader import SafeLoader,FullLoader
host="0.0.0.0"
port = 5000

app = Flask(__name__)

@app.route('/')
def on():
    return 'hello world'

@app.route('/config' ,methods = ['GET','POST'])
def on1():
    api1 = open("config.yaml",'r')
    data = yaml.load(api1,Loader=FullLoader)
    data = data["box1"]["cmd"]
    return data




if __name__ == '__main__':
    app.run(host,port)

