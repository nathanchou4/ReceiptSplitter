class ReceiptItem:
    accounts = []  #List of accounts / names splitting an item

    def __init__(self, item, price):
        self.item = item
        self.price = price

    def add_account(self, account):
        self.accounts.append(account)

    def calc_split(self):
        for account in self.accounts:
            account.add_expense(self.price / len(self.accounts))

    def __repr__(self):
        return '{0} - {1}'.format(self.item, self.price)
