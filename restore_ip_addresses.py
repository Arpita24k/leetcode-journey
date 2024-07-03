from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(start: int, path: List[str]):
            # If we have 4 segments and we've used all digits in the string
            if len(path) == 4 and start == len(s):
                result.append(".".join(path))
                return
            # If we have 4 segments but still have digits left, or vice versa, it's invalid
            if len(path) == 4 or start == len(s):
                return
            
            # Try segments of length 1 to 3
            for length in range(1, 4):
                if start + length <= len(s):
                    segment = s[start:start + length]
                    # Check if the segment is valid
                    if (segment[0] == '0' and len(segment) > 1) or int(segment) > 255:
                        continue
                    # Recur with the chosen segment added to the path
                    backtrack(start + length, path + [segment])
        
        result = []
        backtrack(0, [])
        return result

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    s1 = "25525511135"
    s2 = "0000"
    s3 = "101023"
    
    print(solution.restoreIpAddresses(s1))  # Output: ["255.255.11.135", "255.255.111.35"]
    print(solution.restoreIpAddresses(s2))  # Output: ["0.0.0.0"]
    print(solution.restoreIpAddresses(s3))  # Output: ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]
