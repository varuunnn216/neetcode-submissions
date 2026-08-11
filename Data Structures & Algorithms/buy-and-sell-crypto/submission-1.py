class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            current_price = prices[i]

            potential_profit = current_price - min_price

            max_profit = max(potential_profit, max_profit)

            min_price = min(current_price, min_price)

        return max_profit