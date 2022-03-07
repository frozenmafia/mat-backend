from atexit import register
from distutils.log import debug
from xml.dom.domreg import registered
from flask import Flask, request
import json

app = Flask(__name__)

registered_users = []

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/login",methods=['POST'])
def login():
    print(request.data)
    global registered_users
    data_string = convert_byte_to_string(request.data)
    print(data_string)
    data_json = json.dumps(data_string)
    registered_users = registered_users + [data_json]

    save_data()


    return 'lol'


def save_data():
    global registered_users
    with open("data.json","w") as file:
        file.write("".join(registered_users))

def convert_byte_to_string(data):
    return data.decode('utf-8')

if __name__ == '__main__':
    app.run(debug = True)