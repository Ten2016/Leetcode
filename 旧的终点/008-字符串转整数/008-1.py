class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # 96.61%
        INF_MAX=2**31-1
        INF_MIN=-2**31
        f,sigf=True,True
        res=0
        for i in str:
            if f:
                if i=='+':
                    f=False
                    continue
                if i=="-":
                    f=False
                    sigf=False
                    continue
            if i==' ':
                if f:
                    continue
                else:
                    break
            if '0'<=i<='9':
                res=(res*10+int(i))
                f=False
            else:
                break
        if not sigf:
            res=-res
        if INF_MIN>res:
            return INF_MIN
        elif res>INF_MAX:
            return INF_MAX
        else:
            return res