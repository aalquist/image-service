from flask import Flask
from flask import request
from flask import Response
from flask import Flask, send_file


from PIL import Image, ImageDraw, ImageFont
import os
import io
from io import BytesIO

from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

    return "Hello World! Today is: {}".format(date_time)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello_name(name=None):
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    if name is not None:
        return "Hello {}, Today is: {}".format(name, date_time)
    else:
        return "Hello World! Today is: {}".format(date_time)

@app.route('/save-img/')
@app.route('/save-img/<name>')
def save_img_name(name=None):
    dir_path = os.path.dirname(os.path.realpath(__file__))

    im = Image.new('RGBA', (500,500) )

    draw = ImageDraw.Draw(im)

    fontFile = "{}/fonts/Roboto-Bold.ttf".format( dir_path )
    font = ImageFont.truetype(font=fontFile, size=20)

    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

    if name is None:
        printList = ["Hello", "World", date_time]
    else:
        printList = ["Hello",name, date_time]

    increment = 25
    pos = 20
    for txt in printList:
        pos = pos + increment
        draw.text((20, pos), txt, font=font)

    outfilename = "static/hello-world-timestamp.png"
    absoluteOutfilename = "{}/{}".format( dir_path, outfilename )

    im.save(absoluteOutfilename)

    output =  "saved and updated /{} with:\n{}".format(outfilename, "\n".join(printList))

    resp = Response(output)
    resp.headers['Content-Type'] = 'text/plain'
    return resp

@app.route('/gen-img/')
@app.route('/gen-img/<name>')
def gen_img(name=None):
    
    im = Image.new('RGBA', (500,500) )

    draw = ImageDraw.Draw(im)

    dir_path = os.path.dirname(os.path.realpath(__file__))
    fontFile = "{}/fonts/Roboto-Bold.ttf".format( dir_path )
    font = ImageFont.truetype(font=fontFile, size=20)

    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

    if name is None:
        printList = ["Hello", "World", date_time]
    else:
        printList = ["Hello",name, date_time]

    increment = 25
    pos = 20
    for txt in printList:
        pos = pos + increment
        draw.text((20, pos), txt, font=font)

    bio = BytesIO()
    im.save(bio, format='png')
    bio.flush()

    return Response(bio.getvalue(), mimetype="image/png", direct_passthrough=True)

    
if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)