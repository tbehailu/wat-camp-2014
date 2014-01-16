from operator import add, sub, mul
def square(x):
    """Return x squared."""
    return x * x

# Q1.


def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        op = sub
    else:
        op = add
    return op(a, b)

# Q2.

def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest of a, b, c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    "*** YOUR CODE HERE ***"

    x = max(a,b)
    y = max(b,c)
    
    return x*x + y*y

# Q3.

def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and false_result otherwise."""
    if condition:
        return true_result
    else:
        return false_result


# Q4.
def product(n, term):
    """Return the product of the first n terms in a sequence.

    term -- a function that takes one argument

    >>> product(4, square)
    576
    """
    "*** YOUR CODE HERE ***"
    x = 1
    y = 1
    while x < n:
        x = x+1
        y = y*(term(x))
    return y

def factorial(n):
    """Return n factorial by calling product.

    >>> factorial(4)
    24
    """
    "*** YOUR CODE HERE ***"
    return product(n, abs)

# Q5.
def accumulate(combiner, start, n, term):
    """Return the result of combining the first n terms in a sequence."""
    
    "*** YOUR CODE HERE ***"
    
    """
    >>> accumulate(mul, 1, 4, square)
    576
        
    """
    
    x = start
    y = 1
    while y<n:
        y = y + 1
        x = combiner(x,term(y));
    return x


def summation_using_accumulate(n, term):
    """An implementation of summation using accumulate.

    >>> summation_using_accumulate(4, square)
    30
    """
    "*** YOUR CODE HERE ***"
    
    return accumulate(add, 1, n, term)

def product_using_accumulate(n, term):
    """An implementation of product using accumulate.

    >>> product_using_accumulate(4, square)
    576
    """
    "*** YOUR CODE HERE ***"
    
    return accumulate(mul, 1, n, term)

# Q6.

def double(f):
    """Return a function that applies f twice.

    f -- a function that takes one argument

    >>> double(square)(2)
    16
    """
    "*** YOUR CODE HERE ***"
    
    return lambda x: f(f(x))