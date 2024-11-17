"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.
"""
def findNeedle(haystack, needle):
    # Check if needle is empty
    if not needle:
        return 0

    # Iterate through haystack to find the needle
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i + len(needle)] == needle:
            return i

    # If needle is not found, return -1
    return -1

print(findNeedle("sadbutsad", "sad")) # 0
print(findNeedle("leetcode", "code")) # 4
print(findNeedle("hello", "low")) # -1