from flask import Flask
import random


app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to my page'

@app.route('/dice')
def dice():
    x = random.randint(1,6)
    return f'{x}'
