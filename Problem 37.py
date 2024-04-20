from sympy import isprime

def find_truncatable_primes():
    # Single digit primes are not considered truncatable
    single_digit_primes = {2, 3, 5, 7}
    
    # Helper function to check if a number is left and right truncatable
    def is_truncatable(prime):
        # Convert number to string for manipulation
        str_prime = str(prime)
        
        # Check left truncatable
        for i in range(1, len(str_prime)):
            if not isprime(int(str_prime[i:])) or not isprime(int(str_prime[:-i])):
                return False
        return True
    
    # List to store truncatable primes
    truncatable_primes = []
    
    # Start checking from the first 2-digit prime
    current_number = 11
    
    while len(truncatable_primes) < 11:
        # If the number is prime and is truncatable, add it to the list
        if isprime(current_number) and is_truncatable(current_number):
            truncatable_primes.append(current_number)
        
        # Increment current_number to check the next potential prime
        current_number += 2
    
    # Return the list of truncatable primes
    return truncatable_primes

# Find the truncatable primes and calculate their sum
truncatable_primes = find_truncatable_primes()
sum_truncatable_primes = sum(truncatable_primes)
print(truncatable_primes, sum_truncatable_primes)
