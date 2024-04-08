# Find the sum of the digits in the number 100!

def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * recursive_factorial(n-1)

def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

print(sum_of_digits(recursive_factorial(100)))
recursive_factorial(100)