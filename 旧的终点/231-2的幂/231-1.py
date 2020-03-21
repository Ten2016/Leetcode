class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==0:
            return False
        else:
            while n:
                if n&1 and n!=1:
                    return False
                n>>=1
            return True