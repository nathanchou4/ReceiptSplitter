from ReceiptItem import ReceiptItem
from Account import Account

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Local Host!!!"
#
# receipt = []
# item = input('Enter an item: ')
# price = input('Enter the price of the item ')
# receiptItem = ReceiptItem(item, price)
# receipt.append(receiptItem)
#
# print(receipt)
