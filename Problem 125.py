# Find the sum of all the numbers less than 10^n
## that are both palindromic and can be written as the sum of consecutive squares.

def is_palindrome(num):
    """Check if a number is a palindrome."""
    return str(num) == str(num)[::-1]

def sum_of_consecutive_squares(n):
    """Check if a number can be written as the sum of consecutive squares."""
    for start in range(1, int(n**0.5)+1):
        total = 0
        for i in range(start, int(n**0.5)+1):
            total += i*i
            if total == n:
                return True
            elif total > n:
                break
    return False

def find_palindromic_sums(limit):
    """Find all palindromic numbers that can be written as the sum of consecutive squares and are less than the given limit."""
    palindromic_sums = []
    # Iterate over the range to find palindromic numbers
    for num in range(1, limit):
        if is_palindrome(num) and sum_of_consecutive_squares(num):
            palindromic_sums.append(num)
    return palindromic_sums

# Due to computation limits, we will try a much smaller range first
small_limit = 1000000  # Adjust this as needed to stay within computation limits
palindromic_sums_small = find_palindromic_sums(small_limit)
print(palindromic_sums_small)
print("Sum of palindromic sums:", sum(palindromic_sums_small))
