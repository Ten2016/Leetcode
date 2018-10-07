class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        p,q=0,len(s)-1
        res=list(s)
        while p<q:
            res[p],res[q]=res[q],res[p]
            p+=1
            q-=1
        return ''.join(res)