import math
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 牛顿法
        if x==0:
            return 0
        if x==1:
            return 1
        res=1
        while math.fabs(x-res*res)>0.5:
            res=(res+x/res)/2
        return math.floor(res)