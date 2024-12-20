'''
- PROBLEM: Given two strings s and t, return true if the two strings are anagrams 
of each other, otherwise return false.

* An anagram is a string that contains the exact same characters as another 
string, but the order of the characters can be different.

- DIFFICULTY: Easy
'''
# ------------------------------------------------------------------------------

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        for i in s:
            if s.count(i) != t.count(i): 
                return False

        return True

# ------------------------------------------------------------------------------
'''
TIME COMPLEXITY: O(n^2)
SPACE COMPLEXITY: O(1)
'''