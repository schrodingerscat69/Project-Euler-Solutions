#include <iostream>

// Module value to keep only the last 10 digits 

const long long MOD = 10000000000LL;

// Function to perform modular arithmetic
long long mod_pow(long long base, long long exp, long long mod)
{
	long long result = 1;

	while (exp > 0)
	{
		if (exp % 2 == 1)
		{
			result = (result * base) % mod;
		}

		base = (base * base) % mod;
		exp /= 2;
	}

	return result;
}

// Driver code 
int main()
{
	long long sum = 0;

	// Iterate from n=1 to n=1000 and calculate the sum of n^n % MOD
	for (int n = 1; n <= 1000; n++)
	{
		sum = (sum + mod_pow(n,n, MOD)) % MOD;
	}

	std::cout << "The last 10 digits of the series are: " << sum << std::endl;

	return 0;
}
