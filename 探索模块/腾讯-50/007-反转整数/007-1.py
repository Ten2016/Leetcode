class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 98.41
        if x>=0:
            flag=True
        else:
            flag=False
            x=-x
        res=list(str(x))
        res.reverse()
        x=int(''.join(res))
        x=x if flag else -x
        return x if -2**31<=x<2**31 else 0