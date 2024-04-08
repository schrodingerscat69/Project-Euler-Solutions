# Function to calculate r_max for each a
def calculate_r_max(a):
    # r_max is maximum when n is odd, and for large n, r_max stabilizes at 2*a
    return 2 * a

# Calculate sum of r_max for each a from 3 to 1000
r_max_sum = sum(calculate_r_max(a) for a in range(3, 1001))

print(r_max_sum)
