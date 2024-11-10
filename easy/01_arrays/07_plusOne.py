"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.
"""

def plusOne_0(digits):
    # Convert the array to a number
    num = int(''.join(map(str, digits)))

    # Increment the number by one
    num += 1

    # Convert the incremented number back to an array
    result = [int(digit) for digit in str(num)]

    return result
# test plusOne function
test_0 = [1, 2, 3]
print('plusOne_0:', plusOne_0(test_0))  # Output: [1, 2, 4]


# Alternate solution
def plusOne_1(digits):
    # Start from the last digit and work backwards
    for i in range(len(digits) - 1, -1, -1):
        # If the current digit is less than 9, increment it and return
        if digits[i] < 9:
            digits[i] += 1
            return digits
        # If the digit is 9, set it to 0 and carry over
        digits[i] = 0

    # If all digits were 9, we need to add a 1 at the beginning
    return [1] + digits


# Test the function with an example
test_1 = [1, 0, 9]
print('plusOne_1:', plusOne_1(test_1))  # Output should be [1, 1, 0]