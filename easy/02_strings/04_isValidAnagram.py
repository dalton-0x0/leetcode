"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.


Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""
def isAnagram(s, t):
    # Check if the lengths of the strings are equal
    if len(s) != len(t):
        return False

    # Create a dictionary to store character counts
    char_count = {}

    # Count the occurrences of characters in string s
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Decrement the counts for characters in string t
    for char in t:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] < 0:
            return False

    # Check if all counts are zero
    return all(count == 0 for count in char_count.values())

print('Solution #1')
print(isAnagram('anagram', 'nagaram')) # True
print(isAnagram('rat', 'car')) # False
print(isAnagram('rat', 'tar')) # True
print(isAnagram('rat', 'tara'), '\n') # False

# Alternate solution:
def isAnagram_2(s: str, t: str) -> bool:
    # If lengths are different, they cannot be anagrams
    if len(s) != len(t):
        return False

    # Create frequency dictionary for both strings
    count_s = {}
    count_t = {}

    for char in s:
        count_s[char] = count_s.get(char, 0) + 1

    for char in t:
        count_t[char] = count_t.get(char, 0) + 1

    # Compare frequency dictionaries
    return count_s == count_t

print('Solution #2')
print(isAnagram_2('anagram', 'nagaram')) # True
print(isAnagram_2('rat', 'car')) # False
print(isAnagram_2('rat', 'tar')) # True
print(isAnagram_2('rat', 'tara')) # False
