from cgi import test
import requests
import os
from dotenv import load_dotenv

class CurrencyConversion():
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currency = self.data["conversion_rates"]
    
    




load_dotenv()
key = os.getenv("KEY")





url = "https://v6.exchangerate-api.com/v6/" + key + "/latest/USD"


testing = CurrencyConversion(url)

print(testing.currency["USD"])