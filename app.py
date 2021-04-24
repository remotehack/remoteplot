from flask import Flask, request
from pyaxidraw import axidraw
import json
import time

app = Flask(__name__, 
    static_url_path='', 
    static_folder='static')

@app.route('/', methods=['GET'])
def hello_world():
    return app.send_static_file('index.html')


@app.route('/', methods=['POST'])
def draw():
    # x = int(request.form['x'])
    # y = int(request.form['y'])

    json = request.get_json()

    print(json)


    ad = axidraw.AxiDraw()          # Initialize class
    ad.interactive()                # Enter interactive context
    ad.connect()                    # Open serial port to AxiDraw 


    ad.options.units = 2 # Millimeters
    ad.options.pen_pos_up = 30
    ad.options.pen_pos_down = 60
    ad.update()

    ad.moveto(0,0)
    ad.moveto(json[0][0],json[0][1])

    for point in json:
        time.sleep(0.1)
        ad.lineto(point[0],point[1])
        print(point)


    print("Finished")
    ad.penup()
    ad.moveto(0,0)

    # ad.pendown()


    ad.disconnect()                 # Close serial port to AxiDraw

    return "YAY"


