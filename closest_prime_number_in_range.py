class Solution:
    def closestPrimes(self, left: int, right: int):
        # Step 1: Use Sieve of Eratosthenes to find all primes up to 'right'
        MAX_N = right + 1
        is_prime = [True] * MAX_N
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

        for num in range(2, int(MAX_N**0.5) + 1):
            if is_prime[num]:
                for multiple in range(num * num, MAX_N, num):
                    is_prime[multiple] = False

        # Step 2: Extract primes in the given range
        primes = [num for num in range(left, right + 1) if is_prime[num]]

        # Step 3: Find the closest prime pair
        if len(primes) < 2:
            return [-1, -1]

        min_gap = float('inf')
        closest_pair = [-1, -1]

        for i in range(len(primes) - 1):
            gap = primes[i + 1] - primes[i]
            if gap < min_gap:
                min_gap = gap
                closest_pair = [primes[i], primes[i + 1]]

        return closest_pair

# Example Test Cases
solution = Solution()
print(solution.closestPrimes(10, 19))  # Output: [11, 13]
print(solution.closestPrimes(4, 6))    # Output: [-1, -1]
