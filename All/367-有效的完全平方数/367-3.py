import math
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        v=math.sqrt(num)
        res=False if v-int(v) else True
        return res