class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        # Contar as frequências dos caracteres em 's'
        for i in s:
            if s.count(i) != t.count(i):  # Verificar se a quantidade do caractere em 's' é igual a de 't'
                return False

        return True
        