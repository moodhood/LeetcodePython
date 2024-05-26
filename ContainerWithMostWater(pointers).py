class Solution:
    def maxArea(self, height: list[int]) -> int:
        res = 0 
        l, r  = 0, len(height)-1

        while l < r: 
            area = (r-l)*min(height[r],height[l])
            res = max(area, res)
            
            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                #either l += 1 or r -= 1
                r -= 1
        return res 