import requests
import os
from dotenv import load_dotenv

class CurrencyConversion():
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currency = self.data["conversion_rates"]
    
    def conversion(self, from_currency, to_currency, amount):
        initial_amount = amount

        if from_currency != "USD":
            amount = amount / self.currency[from_currency]
        
        amount = round(amount * self.currency[to_currency], 4)
        return amount

class CurrencyConversionUI():
    pass


load_dotenv()
key = os.getenv("KEY")





url = "https://v6.exchangerate-api.com/v6/" + key + "/latest/USD"


testing = CurrencyConversion(url)


# Printed out all the keys for the currency codes
print(list(testing.currency.keys()))
