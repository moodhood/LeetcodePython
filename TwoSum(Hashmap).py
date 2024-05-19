class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for num in range (0, len(nums)):
            if(target - nums[num] in hashmap):
                return [hashmap[target - nums[num]],num]
            hashmap[nums[num]] = num
            
solution_intance = Solution()
print(solution_intance.twoSum([1,2,3,4], 7))
