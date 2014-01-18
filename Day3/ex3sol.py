# Q1
class VendingMachine(object):
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('crab', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.restock(2)
    'Current crab stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your crab and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your crab.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    """
    "*** YOUR CODE HERE ***"
    
    def __init__(self, product, price):
        self.product = product
        self.price = price
        self.stock = 0
        self.balance = 0
    def vend(self):
        if self.stock == 0:
            return 'Machine is out of stock.'
        if self.balance < self.price:
            return 'You must deposit $' + str(self.price-self.balance) + ' more.'
        change = self.balance-self.price
        self.balance = 0
        self.stock -= 1

        if change != 0:
            return 'Here is your ' + self.product + ' and $' + str(change) +' change.'
        return 'Here is your ' + self.product + '.'
            
    def restock(self,more_stock):
        self.stock += more_stock
        return 'Current crab stock: ' + str(self.stock)
    def deposit(self, amount):
        if self.stock != 0:
            self.balance += amount
            return 'Current balance: $' + str(self.balance)
        return 'Machine is out of stock. Here is your $' + str(amount) + '.'

