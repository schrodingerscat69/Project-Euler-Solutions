# Returns the number of reversible numbers from 1 to n.

def reversible_numbers(n):
    reversible_list = []
    for i in range (1,n):
        reverse_i = int(str(i)[::-1])
        total = i + reverse_i
        if len(str(reverse_i)) != len(str(i)):
            continue
        if all(int(digit) % 2 == 1 for digit in str(total)):
            reversible_list.append(i)
    return len(reversible_list)

print(reversible_numbers(10000000))
