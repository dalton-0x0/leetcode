'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
'''

def removeDuplicates(nums):
    # Initialize the slow pointer
    slow = 0
 
    if not nums:
        return 0
 
    # Iterate with the fast pointer
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            # Found a new unique element, move the slow pointer
            slow += 1
            nums[slow] = nums[fast]
 
    # The number of unique elements is slow + 1
    return slow + 1
 
# Test case 1: General case with duplicates
nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums), nums)  # Output: 5, [1, 2, 3, 4, 5, ...]
