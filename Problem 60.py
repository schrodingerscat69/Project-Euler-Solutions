# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

from sympy import primerange, isprime
from itertools import permutations

# Function to check if concatenating two primes results in a prime
def concatenated_primes(prime_set):
    return all(isprime(int(str(p[0]) + str(p[1]))) for p in permutations(prime_set, 2))

# Generate a list of primes to start with
primes = list(primerange(3, 10000))

# This function will find the set of five primes
def find_prime_set(primes):
    for i, p1 in enumerate(primes):
        for j, p2 in enumerate(primes[i+1:], start=i+1):
            if not concatenated_primes({p1, p2}):
                continue
            for k, p3 in enumerate(primes[j+1:], start=j+1):
                if not concatenated_primes({p1, p2, p3}):
                    continue
                for l, p4 in enumerate(primes[k+1:], start=k+1):
                    if not concatenated_primes({p1, p2, p3, p4}):
                        continue
                    for m, p5 in enumerate(primes[l+1:], start=l+1):
                        if concatenated_primes({p1, p2, p3, p4, p5}):
                            return p1, p2, p3, p4, p5
    return None

# Find the set of five primes
prime_set = find_prime_set(primes)
print(prime_set, sum(prime_set) if prime_set else None)
