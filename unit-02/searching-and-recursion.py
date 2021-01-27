"""
Which logarithmic expression is identical to the following exponential expression?
2^n = 64
- log_2 64 = n

When trying to solve an algorithmic coding challenge, what keywords should you look out for that might alert you that logarithms are involved?
- double
- divide in half
- binary search
- the height of a tree

Below is an example implementation of the binary search algorithm in Python:

def binary_search(item_list, item):
    first = 0
    last = len(item_list) - 1
    while first <= last:
        mid = first + (last - first) // 2
        if item_list[mid] == item :
            return True
        else:
            if item < item_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return False
What must be true for this algorithm to work?

- item_list must be sorted from smallest to greatest
"""

"""
For a given positive integer n determine if it can be represented as a sum of two Fibonacci numbers (possibly equal).

Example

For n = 1, the output should be
fibonacciSimpleSum2(n) = true.

Explanation: 1 = 0 + 1 = F0 + F1.

For n = 11, the output should be
fibonacciSimpleSum2(n) = true.

Explanation: 11 = 3 + 8 = F4 + F6.

For n = 60, the output should be
fibonacciSimpleSum2(n) = true.

Explanation: 60 = 5 + 55 = F5 + F10.

For n = 66, the output should be
fibonacciSimpleSum2(n) = false.
"""

import itertools


def fibonacci_seq_in_range(fib_ceil):
    fib_nums = [0, 1]

    for i in range(2, fib_ceil + 1):
        new_fib = fib_nums[i - 1] + fib_nums[i - 2]

        fib_nums.append(new_fib)

        if new_fib > fib_ceil:
            return fib_nums

    return fib_nums


def fibonacci_simple_sum_2(num):
    if num <= 0:
        return False
    if num == 1:
        return True

    fibs_in_range = fibonacci_seq_in_range(num)

    for fib_a, fib_b in itertools.combinations(fibs_in_range, 2):
        if fib_a + fib_b == num:
            return True

    return False


"""
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search for target in nums. If target exists, then return its index, otherwise, return -1.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Note:

All elements in nums are unique.
The length of nums will be <= 100
The value of each element in nums will be in the range [1, 10000]
"""
def csBinarySearch(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        
        mid = (left + right) // 2
    
        if nums[mid] == target:
            return mid
            
        elif target < nums[mid]:
            right = mid - 1
                
        else:
            left =  mid + 1
            
    return -1


"""
Given an integer array nums sorted in ascending order, and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [1,2,4,5,6,7] might become [4,5,6,7,1,2]).

You should search for target in nums and if found return its index, otherwise return -1.

Example 1:
Input: nums = [6,7,1,2,3,4,5], target = 1
Output: 2

Example 2:
Input: nums = [6,7,1,2,3,4,5], target = 3
Output: 4

Example 3:
Input: nums = [1], target = 2
Output: -1

Your solution should have better than O(n) time complexity over the number of items in the list. There is an O(log n) solution. There is also an O(1) solution.

Note:

1 <= nums.length < 100
1 <= nums[i] <= 100
All values of nums are unique.
Numbers from 1 up to the length of the list will be contained in the list.
"""

def csSearchRotatedSortedArray(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        if nums[left] <= nums[mid]:
            if nums[left] <= target and target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
                
        else:
            if nums[right] >= target and target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
                
    return -1

