class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashmap = {}
        for num in nums:
            if num in hashmap and hashmap[num] >= 1:
                return True
            else:
                hashmap[num] = hashmap.get(num,0) + 1 
        return False
solution_instance = Solution()
nums = [1, 2, 3, 4, 5, 6, 7, 8, -12, 0]
print(solution_instance.containsDuplicate(nums))
