from flask import Flask
app = Flask(__name__)

@app.route('/welcome')
def welcome():
    '''Return simple welcome line'''
    return 'welcome'

@app.route('/welcome/home')
def welcome_home():
    '''Return simple welcome line'''
    return 'welcome home'

@app.route('/welcome/back')
def welcome_back():
    '''Return simple welcome line'''
    return 'welcome back'