class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst=s.split()
        res=[]
        for i in lst:
            p=list(i)
            p.reverse()
            res.append(''.join(p))
        return ' '.join(res)