''' Exercise: Booleans and Conditionals 
    -----------------------------------
    Define a function called sign which takes a numerical argument and returns -1 if it's negative, 1 if it's positive, and 0 if it's 0.
'''
def sing(x):
    if x<0:
        return -1
    elif x>1:
        return 1
    else:
        return (0)

# Modify the definition in the cell below to correct the grammar of our print statement. 
# (If there's only one candy, we should use the singular "candy" instead of the plural "candies")

def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    if total_candies==1:
        print("Splitting", total_candies, "candy")
    else:
        print("Splitting", total_candies, "candies")
    return total_candies % 3

to_smash(91)
to_smash(1)

