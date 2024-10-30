# Interview Concept: Multiple Pointers

In technical interviews, you'll often encounter problems that require the use of multiple pointers with data structures like arrays or linked lists. These pointers enable efficient iteration and mutation of elements. They are particularly useful with sorted structures, as you can make informed assumptions about the order of elements—e.g., in an ascending array, all elements to the left of a current element are less than or equal to it. This reduces the number of operations needed and improves time complexity. Additionally, using pointers often allows for in-place modifications of objects, enhancing efficiency.

Let's look at a sample problem that demonstrates these concepts especially well. This problem is one of the most popular questions on Leetcode.

### Merge Sorted Array:

Given two sorted (ascending order) arrays `nums1` and `nums2`, merge the two arrays so that the final array is also in ascending order.

The catch is that it wants you to perform the operation in-place on the nums1 object. You are given integers `m` and `n`, which represents the number of the elements in nums1 and nums2 respectively. The nums1 array has enough space to accomodate the final merged array, and you do not need to return the array.

For example, given the following:

`
nums1 = [1,3,9,0,0,0,0]
nums2 = [2,4,4,6]
m = 3
n = 4
`
After execution, nums1 should equal `1,2,3,4,4,6,9]`

The first key to simplify this solution is to actually start from the right. Even though gut instinct may be to establish pointers to the first element in nums1 and nums2, starting from the right is simpler because it allows us to replace the empty or '0' values without having to shift slices of the array.

We can use 3 pointers:
1. the rightmost element in nums1 (the actual values [1,3,9]) 
2. the rightmost element in nums2 n2ptr
3. the rightmost element of our merged array (this is actually the last element of nums1, including '0' values) last

To visualize this:
```
      _ ptr1  _ last
     |       |
[1,3,9,0,0,0,0]        # ptr1 is greater than ptr2, set last to ptr1 and decrement ptr1's index
[2,4,4,6]
       |_ptr2

    ptr1   last
   |       |
[1,3,9,0,0,0,9]        # ptr2 is greater than ptr1, set last to ptr2 and decrement ptr2's index
[2,4,4,6]
       |_ptr2

    ptr1 last
   |     |
[1,3,9,0,0,6,9]        # ptr2 > ptr1
[2,4,4,6]
     |_ptr2

  ptr1 last
   |   |
[1,3,9,0,4,6,9]        # ptr2 > ptr1
[2,4,4,6]
   |_ptr2

ptr1 last
   | |
[1,3,9,4,4,6,9]        # ptr1 > ptr2
[2,4,4,6]
 |_ptr2

ptr1_last
 | |
[1,3,3,4,4,6,9]        # ptr2 > ptr1
[2,4,4,6]
 |_ptr2

ptr1_last
 | 
[1,2,3,4,4,6,9]
[2,4,4,6]
 |_ptr2

```

The other key concept with pointers is to know when to terminate the loop. In the example, we can see that the merge is complete once `last` is at the first index of `nums1`. However, we must consider edge cases where either ptr1 or ptr2 are subsituted when either is as a 0 index. If we decrement either value at this point, we will receive an out-of-bounds exception when we try to access the array on the next loop.

To solve for this, our logic should continue to loop while the `last` pointer is greater than 0, but if either ptr1 or ptr2 is less than 0, subsitute last for the opposite pointer element.

The code for this solution looks like the following:

```
from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int):
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
    print(nums1)
    return
```
And here are our test cases to validate the solution:

```
# example case
nums1 = [1,3,9,0,0,0,0]
nums2 = [2,4,4,6]
m = 3
n = 4
merge(nums1, m, nums2, n) # expected value [1,2,3,4,4,6,9]

# edge case 1
nums1 = []
nums2 = []
m = 0
n = 0
merge(nums1, m, nums2, n) # expected value []

# edge case 2
nums1 = [0]
nums2 = [1]
m = 0
n = 1
merge(nums1, m, nums2, n) # expected value [1]
```
Thanks for reading!
