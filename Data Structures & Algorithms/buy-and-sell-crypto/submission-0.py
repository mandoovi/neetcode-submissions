class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price_1 = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            current_profit = prices[i] - price_1
            max_profit = max(current_profit, max_profit)

            if prices[i] < price_1:
                price_1 = prices[i]
            
        return max_profit