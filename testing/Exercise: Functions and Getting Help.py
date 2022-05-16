# Docstrings 

def least_difference(a, b, c):
    """Return the smallest difference between any two numbers
    among a, b and c.
    
    >>> least_difference(1, 5, -5)
    4
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)

# Default arguments
# When we called help(print), we saw that the print function has several optional arguments. 
# For example, we can specify a value for sep to put some special string in between our printed arguments:

print(1, 2, 3, sep=' < ')

# Resultado:  1 < 2 < 3

# Functions Applied to Functions
# Here's something that's powerful, though it can feel very abstract at first. 
# You can supply functions as arguments to other functions. Some example may make this clearer:

def mult_by_five(x):
    return 5 * x

def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)

def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))

print(
    call(mult_by_five, 1),
    squared_call(mult_by_five, 1), 
    sep='\n', # '\n' is the newline character - it starts a new line
)

# Functions that operate on other functions are called "higher-order functions." 
# You probably won't write your own for a little while. But there are higher-order functions built into Python that you might find useful to call.
# Here's an interesting example using the max function.
# By default, max returns the largest of its arguments. 
# But if we pass in a function using the optional key argument, it returns the argument x that maximizes key(x) (aka the 'argmax').

def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5

print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key=mod_5),
    sep='\n',
)

# Exercises 
def round_to_two_places(num):
    """Return the given number rounded to two decimal places. 
    
    >>> round_to_two_places(3.14159)
    3.14
    """
    return round (num, 2)
    pass

# Modify it so that it optionally takes a second argument representing the number of friends the candies are being split between. 
# If no second argument is provided, it should assume 3 friends, as before.

def to_smash(total_candies, n_friends=3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    return total_candies % n_friends

to_smash(57,3)