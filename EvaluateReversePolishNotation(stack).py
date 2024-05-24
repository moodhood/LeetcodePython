class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for str in tokens:
            if(str =="+"):
                stack.append(stack.pop() + stack.pop())
            elif(str =="-"):
                x, y = stack.pop(), stack.pop()
                stack.append(y-x)
            elif(str =="/"):
                x, y = stack.pop(), stack.pop()
                stack.append(int(y/x))
            elif(str =="*"):
                stack.append(stack.pop() * stack.pop())
            else:
                stack.append(int(str))
        return stack[0]