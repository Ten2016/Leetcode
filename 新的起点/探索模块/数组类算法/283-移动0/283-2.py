class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        p=0
        for i in nums:
            if i:
                nums[p]=i
                p+=1
        for i in range(p,len(nums)):
            nums[i]=0