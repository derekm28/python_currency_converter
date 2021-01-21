from flask import Flask, request, redirect, render_template, flash, jsonify #forex-python
from flask_debugtoolbar import DebugToolbarExtension

"""set up class below"""

class Converter():

    def __init__(self, url):

        url = 'https://ratesapi.io'
        self.currencies = request.get(url).json()
        self.curr = self.currencies('rates')


    def find_curr(self, ):
        """finds and returns all possible currencies"""


    def check_valid_curr(curr):
        """checks to see if currency is valid"""

        curr_exist = curr in self.curr
        #valid_curr = self.find()

        if curr_exist:
            return

        else:
            return 'not valid currency'

    def convert(self, converting_from, converting_to, amount):
        """converts currency"""

        intitial_amount = amount
        amount = round(amount * self.currencies[to_currency], 4)
        return amount
