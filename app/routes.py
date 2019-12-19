from app import app
from datetime import datetime
import os.path

indexPath = "/usr/src/app/index.html"
roomPath = "/home/itamar/usr/rooms/"


@app.route('/', methods=['GET'])
def index_page():
    if os.path.isfile(indexPath):
        with open(indexPath, 'r') as f:
            data = f.read()
    else:
        return "no logs available."

    return data


@app.route('/<room>', methods=['GET'])
def room_page(room):
    if os.path.isfile(indexPath):
        with open(indexPath, 'r') as f:
            data = f.read()
    else:
        return "no logs available."

    return data


@app.route('/api/chat/<room>', methods=['GET'])
def chat_room_page(room):
    if os.path.isfile(roomPath + room):
        with open(roomPath + room, 'r') as f:
            data = f.read()
    else:
        return roomPath + room
        # return "chat is currently empty."

    return data
