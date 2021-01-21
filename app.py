from flask import Flask, request, flash, redirect, render_template, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from converter import Converter

app = Flask(__name__)

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


@app.route('/display_currency', methods = ['POST'])
def display_currency():
    """displays conversion at bottom of form"""

    resp = request.form
    from_code = resp["converting_from"].upper()
    to_code = resp["converting_to"].upper()
    amount= float(resp ["amount"])

    print('amount: ', amount)

    exchanged_currency = converter.exchange(from_code, to_code, amount)
    print('EEEEEEEEE: ', exchanged_currency)
    flash(f'{exchanged_currency}', 'alert alert-success')


    # amount = request.json['amount']

    return redirect("/")
