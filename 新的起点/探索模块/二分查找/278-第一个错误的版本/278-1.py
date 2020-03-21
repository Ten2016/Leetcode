# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 使用第二种
        left,right=1,n
        while left<=right:
            mid=(left+right)>>1
            if isBadVersion(mid):
                right=mid-1
            else:
                left=mid+1
        return left
                