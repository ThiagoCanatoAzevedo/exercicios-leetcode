'''
- PROBLEM: Given an array of integers nums and an integer target, return indices 
of the two numbers such that they add up to target.

* You may assume that each input would have exactly one solution, and you may not 
use the same element twice.

* You can return the answer in any order.

- DIFFICULTY: Easy
'''
# ------------------------------------------------------------------------------

class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}
        
        for i, num in enumerate(nums):
            complemento = target - num
            
            if complemento in hashmap:
                return [hashmap[complemento], i]
            
            hashmap[num] = i

# ------------------------------------------------------------------------------
'''
TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
'''
