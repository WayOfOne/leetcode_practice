# Easy question: useful to graph this example out to visualize it

from typing import List


class Solution:
    # O(n) solution since we just loop through the list once
    def maxProfit(self, prices: List[int]) -> int:
        # profits are only values 0 or greater
        profit = 0
        left, right = 0, 1
        while right <= len(prices)-1:
            # profits greater than 0
            if prices[right] > prices[left]:
                diff = prices[right] - prices[left]
                profit = max(profit, diff)
            else:
                # set left pointer to right because we found a new min buying price so any further calculations
                # using the old buying price must generate a smaller profit than if we bought at a lower price
                left = right
            right+=1
        return profit
