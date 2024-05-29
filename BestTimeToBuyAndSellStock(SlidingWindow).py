class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l,r = 0,1
        profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = max(prices[r]-prices[l], profit)
            else:
                l = r  
            r += 1
        return profit
so = Solution()
print(so.maxProfit([5,6,1,8]))
