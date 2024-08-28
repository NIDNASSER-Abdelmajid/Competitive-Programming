class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profits = [0]
        m = 0
        k = len(prices)
        if k == 1:
            return 0
        else:
            min_price = float('inf') 
            for price in prices:
                if price < min_price:
                    min_price = price  
                profit = price - min_price 
                if profit > m:
                    m = profit 

            return m
            