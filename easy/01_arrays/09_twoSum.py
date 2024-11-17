"""
Given an array of integers 'nums' and an integer 'target', return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order
"""

def twoSum(nums, target):
    # Create an empty dictionary to store the complement of each number
    complement_dict = {}

    # Iterate through the array
    for i, num in enumerate(nums):
        # Calculate the complement of the current number
        complement = target - num

        # Check if the complement exists in the dictionary
        if complement in complement_dict:
            # If it does, return the indices of the current number and its complement
            return [complement_dict[complement], i]

        # If not, store the current number and its index in the dictionary
        complement_dict[num] = i

    # If no solution is found, return an empty list
    return []

# Example usage:
num_array= [2, 7, 2, 15]
target_int = 4
print(twoSum(num_array, target_int))  # Output: [0, 2]
