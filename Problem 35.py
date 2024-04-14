# How many circular primes are there below one million?

from sympy import isprime

def rotation(n):
    rotations = []
    for i in range(len(str(n))):
        m = int(str(n)[i:] + str(n)[:i])
        rotations.append(m)
    return rotations

def all_prime(list_rotations):
    prime = all(isprime(num) for num in list_rotations)
    return prime

def circular_primes(n):
    answer = []
    for i in range (2,n):
        if isprime(i):
            if all_prime(rotation(i)):
                answer.append(i)
    return answer
                
print(circular_primes(1000000))
print(len(circular_primes(1000000)))