class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.peeked_value = None  # Buffer to store the next element for peek

    def peek(self):
        # If we already have a peeked value, return it
        if self.peeked_value is None:
            # If no value has been peeked, fetch it from the iterator
            if self.iterator.hasNext():
                self.peeked_value = self.iterator.next()
        return self.peeked_value

    def next(self):
        # If there's a peeked value, return it and clear the buffer
        if self.peeked_value is not None:
            result = self.peeked_value
            self.peeked_value = None
            return result
        else:
            # Otherwise, return the next element from the iterator
            return self.iterator.next()

    def hasNext(self):
        # We have a next element if there's a peeked value or if the iterator has more elements
        return self.peeked_value is not None or self.iterator.hasNext()

# Assume the underlying iterator is implemented like this:
class Iterator:
    def __init__(self, nums):
        self.nums = nums
        self.index = 0

    def next(self):
        if self.hasNext():
            val = self.nums[self.index]
            self.index += 1
            return val
        else:
            raise StopIteration

    def hasNext(self):
        return self.index < len(self.nums)

# Example usage:
nums = [1, 2, 3]
iterator = Iterator(nums)  # Create an iterator from the list [1, 2, 3]
peekingIterator = PeekingIterator(iterator)  # Initialize PeekingIterator

print(peekingIterator.next())    # return 1
print(peekingIterator.peek())    # return 2, does not advance the iterator
print(peekingIterator.next())    # return 2, advances the iterator
print(peekingIterator.next())    # return 3, advances the iterator
print(peekingIterator.hasNext()) # return False, no more elements
