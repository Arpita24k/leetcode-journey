class Solution:
    def maximumBeauty(self, items, queries):
        # Step 1: Sort items based on price
        items.sort()
        processed_items = []
        max_beauty = 0

        for price, beauty in items:
            max_beauty = max(max_beauty, beauty)
            # Avoid duplicates in price to optimize the search
            if not processed_items or processed_items[-1][0] != price:
                processed_items.append((price, max_beauty))
            else:
                # Update the max beauty for the same price
                processed_items[-1] = (price, max_beauty)

        # Step 2: Store queries with their original indices
        queries_with_indices = [(q, idx) for idx, q in enumerate(queries)]
        queries_with_indices.sort()

        # Step 3: Process queries
        answer = [0] * len(queries)
        item_idx = 0
        n = len(processed_items)

        for query_price, idx in queries_with_indices:
            # Move the item_idx to include all items with price <= query_price
            while item_idx < n and processed_items[item_idx][0] <= query_price:
                item_idx += 1
            if item_idx == 0:
                answer[idx] = 0  # No items with price <= query_price
            else:
                # The maximum beauty is the beauty at item_idx - 1
                answer[idx] = processed_items[item_idx - 1][1]

        return answer

# Example usage:
solution = Solution()

# Example 1:
items1 = [[1,2],[3,2],[2,4],[5,6],[3,5]]
queries1 = [1,2,3,4,5,6]
print("Output for Example 1:", solution.maximumBeauty(items1, queries1))
# Expected Output: [2,4,5,5,6,6]

# Example 2:
items2 = [[1,2],[1,2],[1,3],[1,4]]
queries2 = [1]
print("Output for Example 2:", solution.maximumBeauty(items2, queries2))
# Expected Output: [4]

# Example 3:
items3 = [[10,1000]]
queries3 = [5]
print("Output for Example 3:", solution.maximumBeauty(items3, queries3))
# Expected Output: [0]
