"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

1. Whitespace: Ignore any leading whitespace (" ").
2. Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
3. Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the
string is reached. If no digits were read, then the result is 0.
4. Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain
in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should
be rounded to 231 - 1.
Return the integer as the final result.
"""
def myAtoi(s):
    # Define the bounds of a 32-bit signed integer
    int_max = 2 ** 31 - 1
    int_min = -2 ** 31

    # Remove leading whitespace
    s = s.lstrip()

    # If the string is empty after removing whitespace, return 0
    if not s:
        return 0

    # Initialize variables
    sign = 1  # Assume positive sign initially
    result = 0
    i = 0
    n = len(s)

    # Check for sign
    if s[0] in ['-', '+']:
        sign = -1 if s[0] == '-' else 1
        i += 1

    # Process digits
    while i < n and s[i].isdigit():
        result = result * 10 + int(s[i])
        i += 1

    # Apply sign and check for overflow
    result *= sign
    if result < int_min:
        return int_min
    elif result > int_max:
        return int_max
    else:
        return result

print('myAtoi:', myAtoi("42")) # myAtoi: 42
print('myAtoi:', myAtoi("   -42")) # myAtoi: -42
print('myAtoi:', myAtoi("4193 with words")) # myAtoi: 4193
print('myAtoi:', myAtoi("words and 987")) # myAtoi: 0
print('myAtoi:', myAtoi("-91283472332")) # myAtoi: -2147483648