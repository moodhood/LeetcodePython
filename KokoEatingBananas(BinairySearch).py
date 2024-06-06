import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r #k is at least max of piles

        while l <= r: 
            k = (l + r) // 2
            hours = 0

            for bananas in range(0,len(piles)): 
                hours += math.ceil(piles[bananas] / k)
            
            if hours <= h: 
                res = min(k, res)
                l = l
                r = k - 1
            else:
                l = k + 1
                r = r 
        return res