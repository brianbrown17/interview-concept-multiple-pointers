from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
    ptr1 = m - 1
    ptr2 = n - 1
    last = m + n -1
    while last >= 0:
        if ptr2 < 0:
            nums1[last] = nums1[ptr1]
            ptr1 -= 1
        elif ptr1 < 0:
            nums1[last] = nums2[ptr2]
            ptr2 -= 1
        elif nums1[ptr1] > nums2[ptr2]:
            nums1[last] = nums1[ptr1]
            ptr1 -= 1
        else: 
            nums1[last] = nums2[ptr2]
            ptr2 -= 1
        last -= 1
    return nums1

# example case
nums1 = [1,3,9,0,0,0,0]
nums2 = [2,4,4,6]
m = 3
n = 4
print(merge(nums1, m, nums2, n)) # expected value [1,2,3,4,4,6,9]

# edge case 1
nums1 = []
nums2 = []
m = 0
n = 0
print(merge(nums1, m, nums2, n)) # expected value []

# edge case 2
nums1 = [0]
nums2 = [1]
m = 0
n = 1
print(merge(nums1, m, nums2, n)) # expected value [1]
