class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum1,sum2=0,sum(nums)
        for i in range(len(nums)):
            sum2-=nums[i]
            if sum1==sum2:
                return i
            sum1+=nums[i]
        return -1