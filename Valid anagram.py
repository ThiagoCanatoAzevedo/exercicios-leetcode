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

        count_s = {}
        count_t = {}
        
        for char in s:
            count_s[char] = count_s.get(char, 0) + 1
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1
        
        return count_s == count_t

# ------------------------------------------------------------------------------
'''
TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
'''
