"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0
Explanation:
The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1

Constraints:
1 <= s.length <= 105
s consists of only lowercase English letters.
"""

def firstUniqueChar(s):
    # Create a dictionary to store the count of each character
    char_count = {}

    # Count the occurrences of each character
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Find the first character with a count of 1
    for i in range(len(s)):
        if char_count[s[i]] == 1:
            return i

    # If no unique character is found, return -1
    return -1

print('firstUniqueChar_1:', firstUniqueChar('leetcode')) # firstUniqueChar_1: 0
print(firstUniqueChar("loveleetcode"))  # Output: 2
print(firstUniqueChar("aabb"))  # Output: -1

# Alternate solution
def firstUniqueChar_2(s):
    from collections import Counter
    # Count the occurrences of each character
    char_count = Counter(s)

    # Find the first character with a count of 1
    for i in range(len(s)):
        if char_count[s[i]] == 1:
            return i

    # If no unique character is found, return -1
    return -1

print('firstUniqueChar_2:', firstUniqueChar_2('leetcode')) # firstUniqueChar_2: 0
print(firstUniqueChar("loveleetcode"))  # Output: 2
print(firstUniqueChar("aabb"))  # Output: -1
