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
        contador = 0
        while True:
            primVal = nums[contador]
            secVal = nums[contador+1]
        
            soma = primVal+secVal
            
            if(soma == target):
                return(contador, contador+1)
                break
        
            contador+=1

# ------------------------------------------------------------------------------
'''
TIME COMPLEXITY: O(n^2)
SPACE COMPLEXITY: O(1)
'''