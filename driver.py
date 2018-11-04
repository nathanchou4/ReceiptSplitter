from ReceiptItem import ReceiptItem
from Account import Account

r = ReceiptItem("milk", 5.00)
a = Account("Peter")
n = Account("Nathan")
r.add_account(a)
r.add_account(n)
r.calc_split()

print(a.account_holder, "owes ${:.2f}".format(a.expenses))
print(n.account_holder, "owes ${:.2f}".format(a.expenses))
