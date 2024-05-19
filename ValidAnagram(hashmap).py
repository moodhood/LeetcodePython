class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmapx = {}
        hashmapy = {}
        x = map(lambda x:x, s)
        y = map(lambda x:x, t)
        for letter in x:
            hashmapx[letter] = hashmapx.get(letter,0) + 1
        for letter in y:
            hashmapy[letter] = hashmapy.get(letter,0) + 1
        if (hashmapy == hashmapx):
            return True
        else: 
            return False

so = Solution()
so.isAnagram("pra", "rpa")

