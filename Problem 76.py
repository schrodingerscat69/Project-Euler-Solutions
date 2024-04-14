# How many different ways can one hundred be written as a sum of at least two positive integers?

def partition(number):
    # Create a memoization table, initialized to 0
    ways = [0] * (number + 1)
    ways[0] = 1  # There's 1 way to partition 0
    
    # For each number from 1 to the target number
    for i in range(1, number):
        # Update the ways to partition each j from i to the number
        for j in range(i, number + 1):
            ways[j] += ways[j - i]
    
    # Subtract 1 because we don't want to include the number itself (single-partition)
    return ways[number] - 1

# Number of ways to partition 100 into at least two positive integers
number_of_ways = partition(100)
print(number_of_ways)
