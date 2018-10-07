class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        xsum=sum(nums)
        if xsum<S:
            return 0
        elif xsum==S:
            x=2**nums.count(0)
            return x if x else 1
        length=len(nums)
        res=0
        for i in range(2**length):
            xsum=0
            xi=i
            for j in range(length):
                # 如果为1，则加
                if xi&1:
                    xsum+=nums[j]
                else:
                    xsum-=nums[j]
                xi>>=1
            if xsum==S:
                res+=1
        return res