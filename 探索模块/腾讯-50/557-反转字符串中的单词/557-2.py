class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=[]
        p=q=0
        while q<len(s):
            while q<len(s) and s[q]!=' ':
                q+=1
            tmps=list(s[p:q])
            m,n=0,q-p-1
            while m<n:
                tmps[m],tmps[n]=tmps[n],tmps[m]
                m+=1
                n-=1
            res.append(''.join(tmps))
            p=q=q+1
        return ' '.join(res)