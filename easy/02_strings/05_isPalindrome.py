"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric
characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""
def isPalindrome(s):
    # Convert to lowercase and remove non-alphanumeric characters
    s = ''.join(char.lower() for char in s if char.isalnum())

    # Check if the string is equal to its reverse
    return s == s[::-1]

#  Test cases
print('isPalindrome:', isPalindrome('race a car')) # isPalindrome: False
print('isPalindrome:', isPalindrome('A man, a plan, a canal: Panama')) # isPalindrome: True