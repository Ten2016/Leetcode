class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 前100%
        res=s.split()
        if res==[]:
            return 0
        else:
            return len(res[-1])