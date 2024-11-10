"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
"""

def moveZeroes(nums):
    # Initialize a pointer to keep track of the position to place the next non-zero element
    pointer = 0

    # Iterate through the array
    for i in range(len(nums)):
        # If the current element is non-zero
        if nums[i] != 0:
            # Place the non-zero element at the pointer position
            nums[pointer] = nums[i]
            pointer += 1

    # Fill the remaining positions with zeros
    for i in range(pointer, len(nums)):
        nums[i] = 0

# Example usage:
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]
