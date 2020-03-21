class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left,right=0,len(nums)-1
        while left<right:
            mid=(left+right)>>1
            # 中间值大于右边，局部最大值在左边
            if nums[mid]>=nums[mid+1]:
                right=mid
            else:
                left=mid+1
        return left