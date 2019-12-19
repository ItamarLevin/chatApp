from app import app
from datetime import datetime
import os.path
from flask import request, render_template

indexPath = "/usr/src/app/index.html"
roomPath = "/usr/src/app/rooms/"


@app.route('/', methods=['GET'])
def index_page():
    if os.path.isfile(indexPath):
        with open(indexPath, 'r') as f:
            main_page = f.read()
    else:
        return render_template('404.html'), 404

    return main_page


@app.route('/<room>', methods=['GET'])
def room_page(room):
    if os.path.isfile(indexPath):
        with open(indexPath, 'r') as f:
            main_page = f.read()
    else:
        return render_template('404.html'), 404

    return main_page


@app.route('/api/chat/<room>', methods=['GET'])
def chat_room_page(room):
    if os.path.isfile(roomPath + room):
        with open(roomPath + room, 'r') as f:
            data = f.read()
    else:
        return "Chat is currently empty."

    return data


@app.route('/api/chat/<room>', methods=['POST'])
def posting_api(room):
    user_name = request.form["username"]
    msg = request.form["msg"]

    now = datetime.now()  # current date and time
    formatted_time = now.strftime("[%x %X]")

    with open(roomPath + room, 'a') as f:
        f.write("{0} {1}: {2}\n".format(formatted_time, user_name, msg))
    return ""

