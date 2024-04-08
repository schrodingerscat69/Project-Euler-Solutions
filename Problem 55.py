# Returns the Lychrel numbers less than 10000

def is_palindrome(number):
    return str(number) == str(number)[::-1]

def reverse_and_add(number):
    return number + int(str(number)[::-1])

def is_lychrel(number, max_iterations=50):
    for i in range(max_iterations):
        number = reverse_and_add(number)
        if is_palindrome(number):
            return False
    return True

lychrel_numbers = []
lychrel_count = 0
for i in range(1, 10000):
    if is_lychrel(i):
        lychrel_numbers.append(i)
        lychrel_count += 1

print(lychrel_count)
print(lychrel_numbers)