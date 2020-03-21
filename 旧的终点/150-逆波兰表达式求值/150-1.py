class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        dit={'+','-','*','/'}
        stack=[]
        stack.extend(tokens[:2])
        for i in tokens[2:]:
            if i in dit:
                v=eval(stack[-2]+i+stack[-1])
                stack.pop()
                stack.pop()
                stack.append(str(int(v)))
            else:
                stack.append(i)
        return int(stack[0])