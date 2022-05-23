from tools import * 

@app.route('/')
def page0():
    return '0'

app.run(host,port)