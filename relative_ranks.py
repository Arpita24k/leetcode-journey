def findRelativeRanks(score):
    # Pair scores with their indices
    indexed_scores = [(s, i) for i, s in enumerate(score)]
    
    # Sort based on scores in descending order
    indexed_scores.sort(reverse=True, key=lambda x: x[0])
    
    # Create the result array with the same length as the input scores
    result = [""] * len(score)
    
    # Assign ranks based on sorted order
    for rank, (s, i) in enumerate(indexed_scores):
        if rank == 0:
            result[i] = "Gold Medal"
        elif rank == 1:
            result[i] = "Silver Medal"
        elif rank == 2:
            result[i] = "Bronze Medal"
        else:
            result[i] = str(rank + 1)
    
    return result

# Examples
print(findRelativeRanks([5,4,3,2,1]))  # Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
print(findRelativeRanks([10,3,8,9,4]))  # Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
