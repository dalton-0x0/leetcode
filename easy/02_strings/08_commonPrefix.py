"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""
def commonPrefix(strs):
    # Check if the input list is empty
    if not strs:
        return ""

    # Initialize the prefix with the first string in the list
    prefix = strs[0]

    # Iterate through the list of strings
    for i in range(1, len(strs)):
        # While the current string doesn't start with the prefix
        while strs[i].find(prefix) != 0:
            # Shorten the prefix by removing the last character
            prefix = prefix[:-1]

            # If the prefix becomes empty, there is no common prefix
            if not prefix:
                return ""

    # Return the longest common prefix
    return prefix

# Test cases
print(commonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
print(commonPrefix(["dog", "racecar", "car"]))    # Expected output: ""
print(commonPrefix(["interspecies", "interstellar", "interstate"])) # Expected output: "inters"
print(commonPrefix(["throne", "throne"]))         # Expected output: "throne"
print(commonPrefix(["throne"]))                   # Expected output: "throne"
print(commonPrefix([]))                           # Expected output: ""