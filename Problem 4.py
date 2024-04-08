# Find the largest palindrome made from the product of two 3-digit numbers

def find_largest_palindrome(n):
    palindrome = []
    for i in range (1,n):
        for j in range (1,n):
            if str(i*j) == str(i*j)[::-1] and i*j not in palindrome:
                palindrome.append(i*j)
    return max(palindrome)

find_largest_palindrome(1000)