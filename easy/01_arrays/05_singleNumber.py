"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space
"""

def singleNumber(nums):
    # Initialize the result to 0
    result = 0

    # loop through all the elements in the array
    for num in nums:
        # XOR current result with the current number
        result ^= num
    # The result will be the single number
    return result

# test singleNumber
test_nums = [4,1,2,1,2,4,5,6,6]
print('singleNumber:', singleNumber(test_nums))  # Output: 5