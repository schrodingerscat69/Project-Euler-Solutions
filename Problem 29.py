# How many distinct terms are there in the sequence generated by a^b 
##  for 2 <= a <= 100 and 2 <= b <= 100?

answer = set()
for i in range(2,101):
    for j in range(2,101):
        answer.add(i**j) 
print(len(answer))