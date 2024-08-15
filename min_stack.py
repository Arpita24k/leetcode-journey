class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # If the min_stack is empty or the current value is less than or equal to the current minimum, push it onto min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            # Otherwise, push the current minimum again to keep min_stack the same size as stack
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]

# Example usage:
if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())  # return -3
    minStack.pop()
    print(minStack.top())    # return 0
    print(minStack.getMin()) # return -2
