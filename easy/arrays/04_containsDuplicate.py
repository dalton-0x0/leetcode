"""
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.
Example:
Input: nums = [1,2,3,1]
Output: true
Explanation: The element 1 occurs more than once in the array.
"""

def containsDuplicate(nums):
    # Create an empty set to store unique elements
    unique_elements = set()

    # Iterate through the array
    for num in nums:
        # If the element is already in the set, it means it's a duplicate
        if num in unique_elements:
            return True
        # Otherwise, add the element to the set
        unique_elements.add(num)

    # If no duplicates were found, return False
    return False

# test for containsDuplicate
test_nums = [1, 2, 3]
print('containsDuplicate:', containsDuplicate(test_nums))  # Output: False

# Alternative approach
def containsDuplicate2(nums_arr):
    # Sort the array
    nums_arr.sort()

    # Iterate through the sorted array
    for i in range(len(nums_arr) - 1):
        # If the current element is the same as the next element, it's a duplicate
        if nums_arr[i] == nums_arr[i + 1]:
            return True

    # If no duplicates were found, return False
    return False

# test for containsDuplicate2
test_nums_2 = [1, 2, 3, 1]
print('containsDuplicate2:', containsDuplicate2(test_nums_2))  # Output: True
