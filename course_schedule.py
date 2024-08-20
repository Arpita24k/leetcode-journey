class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        # Build the adjacency list
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        # Visited array
        visited = [0] * numCourses
        
        def dfs(course):
            if visited[course] == 1:  # Found a cycle
                return False
            if visited[course] == 2:  # Already fully processed
                return True
            
            # Mark as being visited
            visited[course] = 1
            
            # Visit all the next courses that depend on this one
            for next_course in graph[course]:
                if not dfs(next_course):
                    return False
            
            # Mark as fully processed
            visited[course] = 2
            return True
        
        # Check each course
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    numCourses1 = 2
    prerequisites1 = [[1, 0]]
    print(solution.canFinish(numCourses1, prerequisites1))  # Output: True
    
    # Test Case 2
    numCourses2 = 2
    prerequisites2 = [[1, 0], [0, 1]]
    print(solution.canFinish(numCourses2, prerequisites2))  # Output: False
