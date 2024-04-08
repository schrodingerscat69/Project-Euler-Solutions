# Let d(n) ne defined as the sum of proper divisors of f. If d(a) = b and d(b) = a
## where a is not equivalent to b, then a and b are amicable.
# Evaluate the sum of all the amicable numbers under 10000.

def calc_factors(n):
    factors = []
    for i in range (1,n):
        if n % i == 0:
            factors.append(i)
    return factors

# Example:
print(calc_factors(256))

def amicable(n):
    amicable_numbers = []
    for i in range(1,n):
        a = sum(calc_factors(i))
        if a > i:
            b = sum(calc_factors(a))
            if b == i:
                amicable_numbers.append(a)
                amicable_numbers.append(i)
    total = sum(amicable_numbers)
    return total

print(amicable(10000))
