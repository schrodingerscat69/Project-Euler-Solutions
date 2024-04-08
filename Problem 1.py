# Find the sum of all the multiples of 3 and 5 below 1000

multiples_of_3_and_5 = []
for i in range(1,1001):
    if i%3 ==0 or i%5 == 0:
        multiples_of_3_and_5.append(i)
#print(multiples_of_3_and_5)
print(sum(multiples_of_3_and_5))
