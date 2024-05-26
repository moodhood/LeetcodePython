class Solution:
    def maxArea(self, height: list[int]) -> int:
        res = 0
        for a in range (0, len(height)):
            for b in range(a+1, len(height)):
                area = (b-a)*min(height[b],height[a])
                res = max(res, area)
        return res 
    

