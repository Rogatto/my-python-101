from Models.Account import Account
from Models.Operations import Operations
from Models.Login import Login
from Models.Merchant import Merchant
import uuid

first_account_identity = uuid.uuid4()
first_account = Account('Guilherme', 'Rogatto', 'M', 1000, 'engineer', first_account_identity)
first_login = Login('gui.rogatto', 'Test123@', first_account_identity)

second_account_identity = uuid.uuid4()
second_account = Account('Gustavo', 'Rogatto', 'M', 2000, 'data engineer', second_account_identity)
second_login = Login('gustavo.rogatto', 'Test456@', second_account_identity)

operations = Operations()

print('################################################################')
operations.my_balance(first_account)
print('################################################################')
operations.my_balance(second_account)
print('################################################################')

new_balance =   operations.receive_salary(1000, first_account)

print('Your balance is now with the new salary: %s' % first_account.bank_balance)

merchant_identity = 111
first_merchant = Merchant('McDonalds', merchant_identity)

balance_after_payment = operations.paying_online(200, 
                                       first_account, 
                                       first_merchant)

print('Your balance after payment: %s' % first_account.bank_balance)

operations.transfer_p2p(first_account, second_account, 200)

print('First accounts balance: %s' % first_account.bank_balance)
print('Second accounts balance: %s' % second_account.bank_balance)