'''
- PROBLEM: A phrase is a palindrome if, after converting all uppercase letters
into lowercase letters and removing all non-alphanumeric characters, it reads 
the same forward and backward. Alphanumeric characters include letters and numbers.

* Given a string s, return true if it is a palindrome, or false otherwise

- DIFFICULTY: Easy
'''
# ------------------------------------------------------------------------------

class Solution(object):
    def isPalindrome(self, s):
        s2 = ''
        s = s.lower() 
        for i in s:
            if(i.isalnum()):
                s2 = s2 + i
                
        s = s2
        
        return s2[::-1] == s


# ------------------------------------------------------------------------------
'''
TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
'''
