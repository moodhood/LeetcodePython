class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1Count, s2Count = {},{}
        for i in range(0,len(s1)):
            s1Count[s1[i]] = s1Count.get(s1[i], 0) + 1 

        p1, p2 = 0,0
        while p2 < len(s2):
            s2Count[s2[p2]] = s2Count.get(s2[p2], 0) + 1
            p2 += 1

            if p2 - p1 == len(s1): 
                if s1Count == s2Count: return True

                s2Count[s2[p1]] = s2Count.get(s2[p1]) - 1

                if s2Count[s2[p1]] == 0:
                    del s2Count[s2[p1]]
                p1 += 1

        return False           
    
so = Solution()
if so.checkInclusion("adc", "dcda") == False: print("False")

else: print("True")