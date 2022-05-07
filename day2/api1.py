from flask import Flask, render_template
app = Flask(__name__)

host = "0.0.0.0"
port = 5000

@app.route("/")
def page():
    return "hello"

@app.route('/1')
def page1(name=None):
  return render_template('index.html', name=name)

@app.route('/2')
def page2(name=None):
    return render_template('main.html',name=name)

@app.route('/3')
def page3(name=None):
    return render_template('main.html',name=name)

if __name__ == '__main__':
    app.run(host,port,debug=True)