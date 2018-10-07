class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        for i in range(50000):
            v=i*i
            if v==num:
                return True
            elif v>num:
                return False