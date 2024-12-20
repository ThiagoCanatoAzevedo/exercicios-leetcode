'''
- PROBLEM: Given an array of integers nums which is sorted in ascending order, 
and an integer target, write a function to search target in nums. If target 
exists, then return its index. Otherwise, return -1.

* You must write an algorithm with O(log n) runtime complexity.

- DIFFICULTY: Easy
'''
# ------------------------------------------------------------------------------

class Solution(object):
    def search(self, nums, target):
        if(target in nums):
            return(nums.index(target))
        else:
            return (-1)

# ------------------------------------------------------------------------------
'''
TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
'''