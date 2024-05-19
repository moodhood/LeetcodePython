class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = sorted(map(lambda x:x, s))
        y = sorted(map(lambda x:x, t))
        if(x == y):
            return True
        else: return False


