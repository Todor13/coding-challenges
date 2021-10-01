# https://leetcode.com/problems/best-time-to-buy-and-sell-stock

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        best_buy = float('inf')
        for price in prices:
            if price < best_buy:
                best_buy = price
            else:
                profit = max(profit, price - best_buy)

        return profit
