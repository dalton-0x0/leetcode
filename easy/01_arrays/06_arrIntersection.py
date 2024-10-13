"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must
appear as many times as it shows in both arrays, and you may return the result in any order.
Example:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
"""
from collections import Counter

def intersect(nums1, nums2):
    # Convert the arrays to sets to find the common elements
    set1 = set(nums1)
    set2 = set(nums2)

    # Find the intersection of the two sets
    intersection = set1.intersection(set2)

    # Convert the intersection set back to a list
    result = list(intersection)

    return result

# test intersect function
test_nums1 = [4, 9, 5]
test_nums2 = [9, 4, 9, 8, 4]
print('intersect_1:', intersect(test_nums1, test_nums2))  # Output: [9, 4]

# alternate solution 2
def intersect_2(nums1, nums2):
    # Convert the arrays to sets to find the common elements
    set1 = set(nums1)
    set2 = set(nums2)

    # Find the intersection of the two sets
    intersection = set1 & set2

    # Convert the intersection set back to a list
    result = list(intersection)

    return result

print('intersect_2:', intersect_2(test_nums1, test_nums2))  # Output: [9, 4]

# alternate solution 3
def intersect_3(nums1, nums2):
    # Create frequency counters for both arrays
    count1 = Counter(nums1)
    count2 = Counter(nums2)

    # Initialize a list to store the intersection
    intersection = []

    # Iterate through the counts of the first array
    for num in count1:
        if num in count2:
            # Add the number to the result the minimum number of times it appears in both arrays
            intersection.extend([num] * min(count1[num], count2[num]))

    return intersection

print('intersect_3:', intersect_3(test_nums1, test_nums2))  # Output: [9, 4]
