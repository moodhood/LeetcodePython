class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def backtracking(openCount, closedCount):
            if openCount == closedCount == n:
                res.append("".join(stack))
                return
            if openCount < n:
                stack.append("(")
                backtracking(openCount+1,closedCount)
                stack.pop()
            if closedCount < openCount:
                stack.append(")")
                backtracking(openCount, closedCount+1)
                stack.pop()

        backtracking(0,0)
        return res 