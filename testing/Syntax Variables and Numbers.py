#Add parentheses to the following expression so that it evaluates to 1.
# a = 5 - 3 // 2
a = (5 - 3) // 2
print (a)

# Add parentheses to the following expression so that it evaluates to 0.
# 8 - 3 * 2 - 1 + 1
b = 8 - (3 * 2) - (1 + 1)
print(b)

# Alice, Bob and Carol have agreed to pool their Halloween candy and split it evenly among themselves. 
# For the sake of their friendship, any candies left over will be smashed. 
# For example, if they collectively bring home 91 candies, they'll take 30 each and smash 1.
# Write an arithmetic expression below to calculate how many candies they must smash for a given haul.

# Variables representing the number of candies collected by alice, bob, and carol
alice_candies = 121
bob_candies = 77
carol_candies = 109

to_smash = (alice_candies + bob_candies + carol_candies) % 3