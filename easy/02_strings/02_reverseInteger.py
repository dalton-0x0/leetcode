"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the
signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""

def reverseInteger(x):
    # Convert the integer to a string, reverse it, and convert it back to an integer
    # Check if the reversed integer is within the 32-bit signed integer range
    # If it's not, return 0
    # Otherwise, return the reversed integer
    reversed_int = int(str(abs(x))[::-1])
    if reversed_int > 2**31 - 1:
        return 0
    return reversed_int if x > 0 else -reversed_int

# Alternate approach
def reverseInteger_2(x):
    # Define the 32-bit signed integer range limits
    int_min, int_max = -2 ** 31, 2 ** 31 - 1

    # Determine the sign of the number
    sign = -1 if x < 0 else 1

    # Reverse the digits of the absolute value of x
    reversed_x = int(str(abs(x))[::-1])

    # Reapply the sign
    reversed_x *= sign

    # Check if reversed_x is within the 32-bit signed integer range
    if reversed_x < int_min or reversed_x > int_max:
        return 0

    return reversed_x

print('reverseInteger_1:', reverseInteger(123)) # reverseInteger_1: 321
print('reverseInteger_2:', reverseInteger_2(456)) # reverseInteger_2: 654
print('reverseInteger_1:', reverseInteger(-789)) # reverseInteger_1: -987
