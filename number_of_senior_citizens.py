class Solution:
    def countSeniorPassengers(self, details):
        senior_count = 0  # Initialize a counter for passengers older than 60
        
        for detail in details:  # Loop through each passenger detail in the list
            age = int(detail[11:13])  # Extract the age from the 11th and 12th characters of the string
            
            if age > 60:  # Check if the extracted age is greater than 60
                senior_count += 1  # Increment the senior count
        
        return senior_count  # Return the total count of senior passengers

# Example usage
solution = Solution()
details1 = ["7868190130M7522","5303914400F9211","9273338290F4010"]
details2 = ["1313579440F2036","2921522980M5644"]

print(solution.countSeniorPassengers(details1))  # Output: 2
print(solution.countSeniorPassengers(details2))  # Output: 0
