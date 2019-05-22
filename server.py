from flask import Flask, render_template, request
import random
import model


app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to my page'

@app.route('/roll-dice')
def dice():
    x = random.randint(1,6)
    return f'{x}'

@app.route('/spam-predict')
def spampred():
    return render_template('spam_entry.html')

@app.route('/spam-result',methods=['POST'])
def spam_result():
    form_input = request.form['spam']
    #form_input = 'hi'
    spam = model.predict(form_input)
    return render_template('spam-result.html', spam=spam)
