class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        lowestPrice = prices[0]
        maxProfit = 0

        for price in prices:
            if price < lowestPrice:
                lowestPrice = price

            profit = price - lowestPrice

            if profit > maxProfit:
                maxProfit = profit

        return maxProfit
        