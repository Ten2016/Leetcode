class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 从中心拓展(2n-1个中心)
        x,xi,xj,smax=0,0,0,0
        si,sj=0,0
        length = len(s)
        for i in range(2*length-1):
            xi,xj=i//2,(i+1)//2
            while xi>=0 and xj<length:
                if s[xi]!=s[xj]:
                    leng=xj-xi-1
                    if leng>smax:
                        smax=leng
                        si,sj=xi+1,xi+1+leng
                    break
                xi-=1
                xj+=1
            leng=xj-xi-1
            if leng>smax:
                smax=leng
                si,sj=xi+1,xi+1+leng
        return s[si:sj]