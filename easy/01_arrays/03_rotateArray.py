"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""

def rotateArray(nums, k):
    n = len(nums)
 
    if n == 0:
        return  # No rotation needed for an empty array
 
    k = k % n  # Adjust k if it's larger than n
 
    # Define the helper function reverse within rotate
    def reverse(start, end):
        # This function reverses the elements of nums from index 'start' to 'end'
        while start < end:
            # Swap the elements at indices start and end
            nums[start], nums[end] = nums[end], nums[start]
            # Move towards the middle
            start, end = start + 1, end - 1
 
    # Step 1: Reverse the entire array
    reverse(0, n - 1)
    # Step 2: Reverse the first k elements
    reverse(0, k - 1)
    # Step 3: Reverse the remaining n-k elements
    reverse(k, n - 1)
 
 
# Test case 1: Normal rotation
nums_1 = [1, 2, 3, 4, 5, 6, 7]
rotateArray(nums_1, 4)  # This will internally call reverse() as needed
print('Test case 1:', nums_1)  # Output: [4, 5, 6, 7, 1, 2, 3]
 
# Test case 2: k larger than the array length
nums_2 = [1, 2, 3, 4, 5, 6, 7]
rotateArray(nums_2, 9)  # Internally, reverse() is called appropriately
print('Test case 2:', nums_2)  # Output: [6, 7, 1, 2, 3, 4, 5]
 
# Test case 3: Array of one element
nums_3 = [1]
rotateArray(nums_3, 3)  # Rotation has no effect here
print('Test case 3:', nums_3)  # Output: [1]

# # Test case 4: k is zero
nums_4 = [1, 2, 3, 4, 5, 6, 7]
rotateArray(nums_4, 0)  # No rotation happens
print('Test case 4:', nums_4)  # Output: [1, 2, 3, 4, 5, 6, 7]
 
# Test case 5: Empty array
nums_5 = []
rotateArray(nums_5, 5)  # Empty array remains unchanged
print('Test case 5:', nums_5)  # Output: []
