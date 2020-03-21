class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INF_MAX=2**31-1
        INF_MIN=-2**31
        y=x if x>0 else -x
        res=0
        while y:
            tmp=y%10
            res=res*10+tmp
            y//=10
        res=res if x>0 else -res
        if res>INF_MAX or res<INF_MIN:
            return 0
        return res