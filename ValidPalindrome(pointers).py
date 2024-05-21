class Solution:
    def isPalindrome(self, s: str) -> bool:
        def alphnumerical(c):
            return (ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9') or  ord('A') <= ord(c) <= ord('Z'))

        leftpointer = 0 
        rightpointer = len(s) - 1
        while(leftpointer < rightpointer):
            while (leftpointer < rightpointer and alphnumerical(s[leftpointer]) == False):
                leftpointer += 1
            while (rightpointer > leftpointer and alphnumerical(s[rightpointer]) == False):
                rightpointer -= 1
            if(s[leftpointer].lower() != s[rightpointer].lower()):
                return False
            leftpointer += 1
            rightpointer -= 1
        return True
