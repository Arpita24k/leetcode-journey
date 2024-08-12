import heapq

class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.min_heap = []
        # Initialize the heap with the given numbers
        for num in nums:
            self.add(num)

    def add(self, val):
        # Add the value to the heap if the heap is not full
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        # If the heap is full, push the new value and pop the smallest one
        elif val > self.min_heap[0]:
            heapq.heapreplace(self.min_heap, val)
        
        # The kth largest element is the smallest element in the heap
        return self.min_heap[0]

# Example usage:
if __name__ == "__main__":
    # Initialize the KthLargest object with k=3 and initial stream [4, 5, 8, 2]
    kthLargest = KthLargest(3, [4, 5, 8, 2])
    
    # Process the add operations and print the results
    print(kthLargest.add(3))  # Output: 4
    print(kthLargest.add(5))  # Output: 5
    print(kthLargest.add(10)) # Output: 5
    print(kthLargest.add(9))  # Output: 8
    print(kthLargest.add(4))  # Output: 8
