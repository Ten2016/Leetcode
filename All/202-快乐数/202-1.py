class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dit={}
        cdit={}
        for i in range(10):
            dit[i]=i*i
        while True:
            m=0
            while n:
                m+=dit[n%10]
                n//=10
            if m==1:
                return True
            if m in cdit:
                return False
            else:
                cdit[m]=1
            n=m