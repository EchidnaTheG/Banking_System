class Account:
    def __init__(self,account_num, account_type, balance, currency, status, opening_date, owner):
        self.account_num = account_num
        self.type = account_type
        self.balance = balance 
        self.currency = currency
        self.status= status
        self.opening_date= opening_date
        self.owner = owner
    