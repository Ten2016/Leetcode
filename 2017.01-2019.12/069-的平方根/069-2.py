import math
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Å£¶Ù·¨
        res=1
        while math.fabs(x-res*res)>0.5:
            res=(res+x/res)/2
        return math.floor(res)