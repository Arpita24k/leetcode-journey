class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Split the version strings by '.'
        v1_parts = version1.split('.')
        v2_parts = version2.split('.')
        
        # Determine the maximum length of the two version lists
        max_length = max(len(v1_parts), len(v2_parts))
        
        # Compare each corresponding revision part
        for i in range(max_length):
            # If a part is missing, treat it as 0
            v1_revision = int(v1_parts[i]) if i < len(v1_parts) else 0
            v2_revision = int(v2_parts[i]) if i < len(v2_parts) else 0
            
            if v1_revision < v2_revision:
                return -1
            elif v1_revision > v2_revision:
                return 1
        
        # All revisions are equal
        return 0

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    version1 = "1.2"
    version2 = "1.10"
    print(solution.compareVersion(version1, version2))  # Output: -1
    
    # Test Case 2
    version1 = "1.01"
    version2 = "1.001"
    print(solution.compareVersion(version1, version2))  # Output: 0
    
    # Test Case 3
    version1 = "1.0"
    version2 = "1.0.0.0"
    print(solution.compareVersion(version1, version2))  # Output: 0
