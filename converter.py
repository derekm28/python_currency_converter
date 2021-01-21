from forex_python.converter import CurrencyCodes, CurrencyRates, RatesNotAvailableError

"""set up class below"""

class Converter():

    def __init__(self):

        self.currency_rates = CurrencyRates()
        self.currency_codes = CurrencyCodes()


    def check_valid_code(self, code):
        """checks to see if currency is valid"""

        return self.currency_codes.get_currency_name(code) is not None

    def exchange(self, converting_from, converting_to, amount):
        """converts currency"""

        print('PPPPPPPPP')

        # try:
        amount = f"{self.currency_rates.convert(converting_from, converting_to, amount):.2f}"
        print('RRRRRRR: ', amount)
        return amount
        # except RatesNotAvailableError:
        #     return None

    # def show_currency():
    #     """displays converted currency amount"""

    #     amount = f"{CurrencyRates().convert(converting_from, converting_to, amount):.2f}"

    #     return amount
