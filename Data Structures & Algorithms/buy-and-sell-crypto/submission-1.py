class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        p = 0
        l = 0
        r = 1
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r += 1
            else:
                p = prices[r] - prices[l]
                r += 1
            maxP = max(maxP, p)
        return maxP