class MyCalendar:

    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.bookings:
            if start < e and end > s:  # Check if there is overlap
                return False
        self.bookings.append((start, end))
        return True


# Testing the MyCalendar class with the provided example
myCalendar = MyCalendar()
test_cases = [(10, 20), (15, 25), (20, 30)]
results = [myCalendar.book(start, end) for start, end in test_cases]
results
