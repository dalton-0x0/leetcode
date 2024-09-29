"""
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.
Example:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
"""
def reverseString(s):
    s.reverse()
    return s

s_arr = ['o', 'l', 'l', 'e', 'h']
s_arr_2 = ['o', 'l', 'l', 'e', 'h']
print('reverseString:', reverseString(s_arr))

# alternate solution
def reverseString_2(s):
    # Initialize two pointers
    left = 0                # Points to the start of the string
    right = len(s) - 1      # Points to the end of the string

    # Continue swapping while the pointers haven't met in the middle
    while left < right:
        # Swap the characters at the left and right pointers
        # This is done using Python's multiple assignment feature
        s[left], s[right] = s[right], s[left]

        # Move the left pointer one step to the right
        left += 1
        # Move the right pointer one step to the left
        right -= 1

    # Return the modified string (which is now reversed)
    return s
print('reverseString_2:', reverseString_2(s_arr_2))
