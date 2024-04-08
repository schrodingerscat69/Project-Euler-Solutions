# Find the difference between the sum of the squares of the first one 
## hundred natural numbers and the square of the sum.

square_sum = 0
total = 0
for i in range (1,101):
    square_sum += i**2
    total += i

print(total**2 - square_sum)
