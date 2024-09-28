class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.deque = [-1] * k  # Initialize deque with -1 (assuming valid elements are >= 0)
        self.size = 0
        self.front = 0
        self.rear = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front = (self.front - 1 + self.k) % self.k  # Move front pointer back
        self.deque[self.front] = value  # Insert value at front
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.deque[self.rear] = value  # Insert value at rear
        self.rear = (self.rear + 1) % self.k  # Move rear pointer forward
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.k  # Move front pointer forward
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + self.k) % self.k  # Move rear pointer back
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[self.front]  # Return the front element

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[(self.rear - 1 + self.k) % self.k]  # Return the rear element

    def isEmpty(self) -> bool:
        return self.size == 0  # Check if the deque is empty

    def isFull(self) -> bool:
        return self.size == self.k  # Check if the deque is full