from flask import Flask
import os

app = Flask(__name__)

path = os.listdir()
 
@app.route('/')

def home():
    return "<h1>{path:}!</h1>"
