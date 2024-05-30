class Solution:
    def search(self, nums: list[int], target: int) -> int:
        return self.binairySearch(0, len(nums)-1, nums, target)
        
    def binairySearch(self, l: int, r: int, nums: list[int], target: int) -> int:
        if l <= r: 
            mid = int(l+r)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target: 
                return self.binairySearch(mid+1,r,nums,target) 
            else:
                return self.binairySearch(l,mid-1,nums,target) 
        return -1
so = Solution()
print(so.search([-1,0,3,5,9,12], 9))