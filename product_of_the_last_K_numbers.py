class ProductOfNumbers:
    def __init__(self):
        # Initialize an empty list to store the numbers.
        self.stream = []
        # Initialize a list to store the prefix products.
        self.prefix_products = [1]  # Start with a product of 1 for convenience.

    def add(self, num: int) -> None:
        # Append the number to the stream.
        self.stream.append(num)
        
        # If num is 0, reset the prefix product.
        if num == 0:
            # After a zero, the product becomes zero for all subsequent elements.
            self.prefix_products = [1]
        else:
            # Multiply the current number with the last product in the list.
            self.prefix_products.append(self.prefix_products[-1] * num)

    def getProduct(self, k: int) -> int:
        # If the length of the stream is less than k, return 0.
        if len(self.stream) < k:
            return 0
        
        # Check if k is greater than the length of prefix_products
        if k > len(self.prefix_products) - 1:
            return 0  # or handle as appropriate
        
        # Compute the product of the last k numbers.
        total_product = self.prefix_products[-1]
        
        # Get the product from the prefix_products list by using the formula:
        # product of last k numbers = prefix_products[-1] / prefix_products[-k-1]
        return total_product // self.prefix_products[-k-1]
