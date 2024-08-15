class Solution:
    def lemonadeChange(self, bills):
        five_count = 0
        ten_count = 0
        
        for bill in bills:
            if bill == 5:
                five_count += 1
            elif bill == 10:
                if five_count == 0:
                    return False
                five_count -= 1
                ten_count += 1
            elif bill == 20:
                if ten_count > 0 and five_count > 0:
                    ten_count -= 1
                    five_count -= 1
                elif five_count >= 3:
                    five_count -= 3
                else:
                    return False
        
        return True

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    bills1 = [5,5,5,10,20]
    print(solution.lemonadeChange(bills1))  # Output: True
    
    # Test Case 2
    bills2 = [5,5,10,10,20]
    print(solution.lemonadeChange(bills2))  # Output: False
    
    # Test Case 3
    bills3 = [5,5,5,10,20,20,20]
    print(solution.lemonadeChange(bills3))  # Output: False
