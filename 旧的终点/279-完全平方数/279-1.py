class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 四平方定理
        # n=4^a*(8*b+7)
        while n%4==0:
            n>>=2
        if n%8==7:
            return 4
        for i in range(n+1):
            pf=i*i
            if pf==n:
                return 1
            elif pf>n:
                break    
        for j in range(n):
            for k in range(j,n):
                pf2=j*j+k*k
                if pf2==n:
                    return 2
                elif pf2>n:
                    break
        return 3