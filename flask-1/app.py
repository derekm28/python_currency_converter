from flask import Flask, request, redirect, render_template, flash, jsonify #forex-python
#from models import db, connect_db, User, Post
from flask_debugtoolbar import DebugToolbarExtension
from converter import Converter

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///users'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'ihaveasecret'

debug = DebugToolbarExtension(app)

converter = Converter()

@app.route('/', methods = ['GET'])
def conversion_form():
    """displays converter form"""
    """has button for conversion"""

    #import pdb
    #pdb.set_trace()

    return render_template('curr_converter.html')


@app.route('/https://api.ratesapi.io/api/latest', methods = ['GET'])
def check_valid_curr():
    """check if currency is valid"""

    curr = request.args['currency']
    response = converter.check_valid_curr(curr)

    return jsonify({'result': response})

@app.route('/convert', methods = ['POST'])
def convert():
    """converts currency"""

    return amount
