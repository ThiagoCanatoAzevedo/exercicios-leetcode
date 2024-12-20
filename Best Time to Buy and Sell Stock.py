'''
- PROBLEM: You are given an array prices where prices[i] is the price of a given
stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and 
choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.

- DIFFICULTY: Easy
'''
# ------------------------------------------------------------------------------

class Solution(object):
    def maxProfit(self, prices):
        menorValor = min(prices)
        indexMenorValor = prices.index(menorValor)

        if(indexMenorValor == len(prices)-1):
            maiorValor = 0
            menorValor = 0
        else:
            maiorValor = max(prices[indexMenorValor:len(prices)])
        
        conta = maiorValor-menorValor

        return(conta)

# ------------------------------------------------------------------------------
'''
TIME COMPLEXITY: O(n^2)
SPACE COMPLEXITY: O(1)
'''