class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        r=list(s)
        r.reverse()
        return ''.join(r)