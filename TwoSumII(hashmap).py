class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        hashmap = {}  # number:index
        p1 = 0
        p2 = len(numbers) - 1

        for num in range(len(numbers)):
            hashmap[numbers[num]] = num + 1  # Store index + 1 to match the 1-based index requirement

        while p1 < p2:
            if numbers[p1] + numbers[p2] == target:
                return [p1 + 1, p2 + 1]
            
            x = target - numbers[p2]
            if x in hashmap and hashmap[x] != p2 + 1:
                if(hashmap[x] > p2+1):
                    return[p2 + 1,hashmap[x]]
                return [hashmap[x], p2 + 1]
            
            p2 -= 1

so = Solution()
print(so.twoSum([1,2,3,4,4,9,56,90],8))



