class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        lp,rp=-1,len(nums)
        i=0
        while i<rp:
            if nums[i]==0:
                lp+=1
                nums[i],nums[lp]=nums[lp],nums[i]
                i+=1
            elif nums[i]==2:
                rp-=1
                nums[i],nums[rp]=nums[rp],nums[i]
            else:
                i+=1