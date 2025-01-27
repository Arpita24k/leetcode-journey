class Solution:
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        # Step 1: Initialize the adjacency matrix
        reachable = [[False] * numCourses for _ in range(numCourses)]
        
        # Mark direct prerequisites
        for pre, course in prerequisites:
            reachable[pre][course] = True

        # Step 2: Floyd-Warshall to compute transitive closure
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if reachable[i][k] and reachable[k][j]:
                        reachable[i][j] = True

        # Step 3: Answer the queries
        result = []
        for u, v in queries:
            result.append(reachable[u][v])

        return result


# ✅ Example Usage:
solution = Solution()

# Test Case 1
numCourses1 = 2
prerequisites1 = [[1, 0]]
queries1 = [[0, 1], [1, 0]]
print(solution.checkIfPrerequisite(numCourses1, prerequisites1, queries1))  # Output: [False, True]

# Test Case 2
numCourses2 = 2
prerequisites2 = []
queries2 = [[1, 0], [0, 1]]
print(solution.checkIfPrerequisite(numCourses2, prerequisites2, queries2))  # Output: [False, False]

# Test Case 3
numCourses3 = 3
prerequisites3 = [[1, 2], [1, 0], [2, 0]]
queries3 = [[1, 0], [1, 2]]
print(solution.checkIfPrerequisite(numCourses3, prerequisites3, queries3))  # Output: [True, True]
