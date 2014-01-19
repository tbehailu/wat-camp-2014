# Q3
def describe ( n ):
""" Returns whether n is abundant , perfect , or deficient .
>>> describe (4) # 1 + 2 < 4
'deficient '
"""
    divisors = sum_divisors(n) - n 
    if divisors == n:
        return ’perfect’ 
    elif divisors > n:
        return ’abundant’ 
    else:
        return ’deficient’

# Q4

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

def interleave_recursive(s0, s1):
    """Interleave recursive lists s0 and s1 to produce a new recursive
    list.

    >>> evens = rlist(2, rlist(4, rlist(6, rlist(8, empty_rlist))))
    >>> odds = rlist(1, rlist(3, empty_rlist))
    >>> interleave_recursive(odds, evens)
    (1, (2, (3, (4, (6, (8, None))))))
    >>> interleave_recursive(evens, odds)
    (2, (1, (4, (3, (6, (8, None))))))
    >>> interleave_recursive(odds, odds)
    (1, (1, (3, (3, None))))
    """
    "*** YOUR CODE HERE ***"

    if s0 == empty_rlist:
        return s1
    return rlist(first(s0),interleave_recursive(s1,rest(s0)))
    

# Q5

def hailstone(n):
    """Print the hailstone sequence starting at n and return its length.

    >>> a = hailstone(10)  # Seven elements are 10, 5, 16, 8, 4, 2, 1
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"

    x = 0
    print(n)
    while n != 1:
        if n%2 != 0:
            n = n*3+1
            x = x+1
        else:
            n = n//2
            x = x+1
        print(n)
    return x+1
