class Solution:
    # Calculates the maximum profit from buying and selling stock once
    def maxProfit(self, prices: List[int]) -> int:
        res = 0  # Stores the maximum profit found so far
        mn = prices[0]  # Tracks the minimum price seen so far (buy price)

        for i in range(1, len(prices)):
            res = max(res, prices[i] - mn)  # Update profit if selling today is better
            mn = min(mn, prices[i])  # Update the minimum price if today's price is lower

        return res  # Return the highest profit found
