class Solution:
    def numTeams(self, rating):
        n = len(rating)
        count = 0

        # Iterate through each soldier as the middle soldier
        for j in range(n):
            left_less = left_greater = right_less = right_greater = 0

            # Count the number of soldiers before j that are less than and greater than rating[j]
            for i in range(j):
                if rating[i] < rating[j]:
                    left_less += 1
                if rating[i] > rating[j]:
                    left_greater += 1

            # Count the number of soldiers after j that are less than and greater than rating[j]
            for k in range(j + 1, n):
                if rating[k] < rating[j]:
                    right_less += 1
                if rating[k] > rating[j]:
                    right_greater += 1

            # Calculate the number of valid teams
            count += left_less * right_greater + left_greater * right_less

        return count

# Test the function with the provided examples
sol = Solution()
print(sol.numTeams([2, 5, 3, 4, 1]))  # Output: 3
print(sol.numTeams([2, 1, 3]))        # Output: 0
print(sol.numTeams([1, 2, 3, 4]))     # Output: 4
