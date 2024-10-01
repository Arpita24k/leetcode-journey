from collections import Counter

class Solution:
    def canArrange(self, arr: list[int], k: int) -> bool:
        remainder_count = Counter()

        # Calculate the remainder for each number in the array
        for num in arr:
            remainder = num % k
            if remainder < 0:
                remainder += k  # Ensure remainder is positive for negative numbers
            remainder_count[remainder] += 1
        
        # Check the pairing conditions
        for remainder in remainder_count:
            # If remainder is 0, we need even count of numbers with remainder 0
            if remainder == 0:
                if remainder_count[remainder] % 2 != 0:
                    return False
            # If remainder is k/2, we also need even count of those numbers
            elif remainder == k - remainder:
                if remainder_count[remainder] % 2 != 0:
                    return False
            else:
                # Check if remainder and k - remainder have the same count
                if remainder_count[remainder] != remainder_count[k - remainder]:
                    return False

        return True
