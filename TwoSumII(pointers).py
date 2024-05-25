class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        p1, p2 = 0, len(numbers)-1
        while p1 < p2:
            sum = numbers[p2] + numbers[p1]
            
            if(sum >= target):
                p2 -= 1 
            elif(sum <= target):
                p1 += 1
            else:
                return[p1+1,p2+1]

