from tools import * 

@app.route('/')
def page_0():
    return 'hello'

if __name__ == '__main__':
    app.run(host,port)