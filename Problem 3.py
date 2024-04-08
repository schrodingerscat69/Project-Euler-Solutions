# Returns the largest prime factor of n.
import sympy 

def calc_factors(n):
    factors = []
    for i in range (1,n+1):
        if n % i == 0:
            factors.append(i)
    return factors
print(calc_factors(28349917))

def prime_numbers(n):
    primes = []
    for i in calc_factors(n):
        if sympy.isprime(i) == True:
            primes.append(i)
    return(max(primes))

prime_numbers(28349917)