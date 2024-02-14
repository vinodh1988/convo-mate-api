from flask import Flask,send_from_directory
from flask_cors import CORS
import os


basedir=os.path.abspath(os.path.dirname(__file__))
translate_key=""

app=Flask(__name__,template_folder='../templates')
CORS(app)

@app.route("/files/<path:path>")
def get_file(path):
    return send_from_directory('../static',path)


