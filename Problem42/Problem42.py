alphabets = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 
    'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 
    'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20
}

with open("0042_words.txt", "r") as file:
    content = file.read()

words = [word.strip().strip('"') for word in content.split(',')]

def calc_sum(word):
    sum = 0
    for char in word:
        if char in alphabets:
            sum += alphabets[char]
    return sum



def is_triangular (num):
    # Base case
    if (num < 0):
        return False
    
    sum, n = 0, 1

    while (sum <= num):
        sum += n
        if (sum == num):
            return True
        n += 1
    return False

ans = []
for ele in words:
    if (is_triangular(calc_sum(ele))):
        ans.append(ele)

print(len(ans))
