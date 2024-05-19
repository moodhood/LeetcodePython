class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for num in range(0,len(nums)):
            for numbers in range(0,len(nums)):
                if (nums[num] + nums[numbers] == target and num != numbers):
                    return [num, numbers]

    
solution_instance = Solution()
print(solution_instance.twoSum([2,7,11,15], 9))

        