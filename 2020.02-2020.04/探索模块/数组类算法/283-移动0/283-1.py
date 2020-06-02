class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i=0
        while i<len(nums):
            if nums[i]:
                p=i
                while p>0 and nums[p-1]==0:
                    p-=1
                nums[i],nums[p]=nums[p],nums[i]
            i+=1