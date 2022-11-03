from flask import Flask
import os

app = Flask(__name__)

path = os.listdir()

# wget https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.pbmm
# wget https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.scorer
 
@app.route('/')

def home():
    return path
