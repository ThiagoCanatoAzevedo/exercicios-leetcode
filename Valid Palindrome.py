class Solution(object):
    def isPalindrome(self, s):
        s2 = ''
        s = s.lower() #declar isso dentro da funcao com o paramentro que recebe a tring

        for i in s:
            if(i.isalnum()):
                s2 = s2 + i
                
        s = s2
        
        return s2[::-1] == s



