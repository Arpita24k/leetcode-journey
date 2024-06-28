class Solution:
    def simplifyPath(self, path: str) -> str:
        # Split the path by '/'
        components = path.split('/')
        stack = []
        
        for component in components:
            if component == "..":
                if stack:
                    stack.pop()  # Move up one directory unless stack is empty
            elif component and component != '.':
                stack.append(component)  # Add the directory to the stack if it's a valid name
        
        # Construct the simplified path
        simplified_path = '/' + '/'.join(stack)
        
        return simplified_path

# Example usage:
solution = Solution()

# Example 1
print(solution.simplifyPath("/home/"))  # Output: "/home"

# Example 2
print(solution.simplifyPath("/home//foo/"))  # Output: "/home/foo"

# Example 3
print(solution.simplifyPath("/home/user/Documents/../Pictures"))  # Output: "/home/user/Pictures"

# Example 4
print(solution.simplifyPath("/../"))  # Output: "/"

# Example 5
print(solution.simplifyPath("/.../a/../b/c/../d/./"))  # Output: "/.../b/d"
