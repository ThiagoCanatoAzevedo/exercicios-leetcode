'''
- PROBLEM: Given an integer array nums, return true if any value appears more 
than once in the array, otherwise return false.

- DIFFICULTY: Easy
'''
# ------------------------------------------------------------------------------

class Solution(object):
    def containsDuplicate(self, nums):
        num_set = set()

        for n in nums:
            if n in num_set:
                return True
            num_set.add(n)
        
        return False
        
# ------------------------------------------------------------------------------
'''
TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
'''