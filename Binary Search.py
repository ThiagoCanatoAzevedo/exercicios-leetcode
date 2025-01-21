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
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1

# ------------------------------------------------------------------------------
'''
TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
'''
