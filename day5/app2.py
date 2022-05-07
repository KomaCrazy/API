from flask import Flask, render_template
app = Flask(__name__)

host = "0.0.0.0"
port = 5000

@app.route('/')
def page():
    return '0'

@app.route('/1')
def page1(name=None):
    return render_template('index.html',name=name)

if __name__ == '__main__' :
    app.run(host,port)
