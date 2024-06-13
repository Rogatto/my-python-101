import qrcode
import uuid

class Operations:

    def receive_salary(self, salary, Account):
        if salary <= 0:
            print('Wrong salary value for the user: ', Account.account_identity)
        else:
            Account.bank_balance = Account.bank_balance + salary
        
    def paying_online(self, amount, Account, Merchant):
        if amount <= 0:
            print('Wrong payment value for the user: ', Account.account_identity)
        elif amount > Account.bank_balance:
            print('You do not have sufficient balance to do this purchase: ', Account.account_identity)
        else:
           print('Payment successful for the user: ' + 'on merchant: ', Merchant.merchant_identity)
           Account.bank_balance = Account.bank_balance - amount
        
    def transfer_p2p(self, FromAccount, ToAccount, amount):
        transaction_uuid = str(uuid.uuid4())
        if amount <= 0:
            print('Transfer peer to peer cannot be negative or 0: ')
        elif FromAccount.bank_balance < amount:
            print('You cannot perform this operation, not sufficient balance to transfer')

        qrcode_transfer = qrcode.make(str(FromAccount.account_identity) + '_' + str(ToAccount.account_identity) + str(amount) + transaction_uuid)
        type(qrcode_transfer)
        qrcode_transfer.save('./temp/transfer-p2p-' + transaction_uuid + '.png' )

        FromAccount.bank_balance = FromAccount.bank_balance - amount
        ToAccount.bank_balance = ToAccount.bank_balance + amount

        print('Peer to peer transfer successed: from ' + str(FromAccount.first_name) + ' to ' + str(ToAccount.first_name) + ' the amount was: ' + str(amount))

    def my_balance(self, Account):
        print('Account: ' + Account.first_name + ' and balance: ' + str(Account.bank_balance))