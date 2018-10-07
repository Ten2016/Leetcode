class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        dit={']':'[','}':'{',')':'('}
        if not s:
            return True
        stack.append(s[0])
        for i in s[1:]:
            if stack and i in dit:
                if stack[-1]==dit[i]:
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        if stack:
            return False
        else:
            return True