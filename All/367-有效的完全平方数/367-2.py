class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i=1
        while num>0:
            num-=i
            i+=2
        if num:
            return False
        else:
            return True