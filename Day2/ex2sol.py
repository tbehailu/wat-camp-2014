# Q1
# Draw environment diargram for the following:

def sum_elems(elem):
    if type(elem) == int:
        return elem
    else:
        return (sum_elems(elem[0]) + sum_elems(elem[1]))

pairs = ((1, 2), (3, 4))
total = sum_elems(pairs)

# Q2.

def summation(n, term):
    """Return the sum of the first n terms of a sequence.
  
    >>> summation(5, lambda x: pow(x, 3))
    225
    """
    total = 0
    k = 1
    while k <= n:
        total = total + term(k)
        k = k + 1
    return total

# Q3.

def double(f):
    """Return a function that applies f twice.

    f -- a function that takes one argument

    >>> double(square)(2)
    16
    """
    "*** YOUR CODE HERE ***"
    
    return lambda x: f(f(x))


# Q4.

def count(s, value):
    """Count the number of occurrences of value in sequence s using a for-loop.
    >>> digits = 1, 8, 2, 8
    >>> count(digits, 8)
    2
    """
    total = 0
    for elem in s:
        if elem == value:
            total = total + 1
    return total

# Q5.

empty_rlist = None

def rlist(first, rest):
    """Construct a recursive list from its first element and the
    rest."""
    return (first, rest)

def first(s):
    """Return the first element of a recursive list s."""
    return s[0]

def rest(s):
    """Return the rest of the elements of a recursive list s."""
    return s[1]


def reverse_rlist_iterative(s):
    """Return a reversed version of a recursive list s.

    >>> primes = rlist(2, rlist(3, rlist(5, rlist(7, empty_rlist))))
    >>> reverse_rlist_iterative(primes)
    (7, (5, (3, (2, None))))
    """
    "*** YOUR CODE HERE ***"
    
    list = (first(s),empty_rlist)
    while rest(s) != empty_rlist:
        s = rest(s)
        list = rlist(first(s),list)
    return list

def reverse_rlist_recursive(s):
    """Return a reversed version of a recursive list s.

    >>> primes = rlist(2, rlist(3, rlist(5, rlist(7, empty_rlist))))
    >>> reverse_rlist_recursive(primes)
    (7, (5, (3, (2, None))))
    """
    "*** YOUR CODE HERE ***"
    
    
    list = (first(s),empty_rlist)
    
    def helper(s,list):
        s = rest(s)
        if rest(s) == empty_rlist:
            return rlist(first(s),list)
        return helper(s,rlist(first(s),list))
    return helper(s,list)



# Q6.
def index_largest(seq):
    """Return the index of the largest element in the sequence.

    >>> index_largest([8, 5, 7, 3 ,1])
    0
    >>> index_largest((4, 3, 7, 2, 1))
    2
    """
    assert len(seq) > 0
    "*** YOUR CODE HERE ***"
    return seq.index(max(seq))

# Q7.

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
        return 'Here is your crab.'
            
    def restock(self,more_stock):
        self.stock += more_stock
        return 'Current crab stock: ' + str(self.stock)
    def deposit(self, amount):
        if self.stock != 0:
            self.balance += amount
            return 'Current balance: $' + str(self.balance)
        return 'Machine is out of stock. Here is your $' + str(amount) + '.'

