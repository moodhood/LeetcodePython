class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ''
        for char in s.lower():
            if('a' <= char <= 'z' or '0' <= char <= '9'):
                res += char
        if(res[::-1] == res):
            return True


