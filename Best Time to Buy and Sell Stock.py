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


solution = Solution()
price1 = [7,1,5,3,6,4]
print(solution.maxProfit(price1))

price2 = [7,6,4,3,1]
print(solution.maxProfit(price2))

price3 =[2,4,1]
print(solution.maxProfit(price3))
