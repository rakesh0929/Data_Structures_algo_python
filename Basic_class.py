class CreditCard():
    """ A Credit Card customer"""
    def __init__(self,customer_name,account_number,bank_name,limit,balance = 0):

        """customer the name of the customer (e.g., Mosh)
             bank the name of the bank (e.g., California Savings )
             acnt the acount identifier (e.g., 5391 0375 9387 5309 )
             limit credit limit (any currency )
        """
        self._customer = customer_name
        self._account = account_number
        self._bank = bank_name
        self._limit = limit
        self._balance = balance

    def get_customer(self):
        return self._customer

    def account_num(self):
        return self._account

    def banker_nam(self):
        return self._bank

    def limit_(self):
        return self._limit

    def my_balance(self):
        return self._balance

    def charge(self,price):
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self,draw):
        self._balance -= draw
        return "payment done"


customer_1 = CreditCard("John Doe","1st Bank","5391 0375 9387 5309",1000,50)
print(customer_1.get_customer())
print(customer_1.account_num())
print(customer_1.limit_())
print(customer_1.banker_nam())
print(customer_1.my_balance())
print(customer_1.charge(200))   ### this will add 200 + 50 and True = 250
print(customer_1.make_payment(100))   ## i am withdrawing 100
print(customer_1.my_balance())  ## if you with draw it will show 150

