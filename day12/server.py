from tools import *

@app.route('/')
def page_0():
    return '9'

if __name__ == '__main__':
    server.on()