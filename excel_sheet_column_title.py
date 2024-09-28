def convertToTitle(columnNumber: int) -> str:
    result = []
    
    # Continue until columnNumber becomes 0
    while columnNumber > 0:
        # Adjust for 1-based index
        columnNumber -= 1
        # Get the current letter (remainder when divided by 26)
        result.append(chr(columnNumber % 26 + ord('A')))
        # Update columnNumber
        columnNumber //= 26
    
    # Since we're appending letters from last to first, reverse the result
    return ''.join(result[::-1])
