from flask import Flask, request

app = Flask(__name__, 
    static_url_path='', 
    static_folder='static')

@app.route('/', methods=['GET'])
def hello_world():
    return app.send_static_file('index.html')


@app.route('/', methods=['POST'])
def draw():
    x = int(request.form['x'])
    y = int(request.form['y'])

    return "TODO: draw %s, %s " % (x, y)

