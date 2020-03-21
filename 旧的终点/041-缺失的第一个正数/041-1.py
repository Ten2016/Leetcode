class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        length=len(nums)
        while i<length:
            if nums[i]>0 and nums[i]<=length and nums[i]!=nums[nums[i]-1]:
                v=nums[i]-1
                nums[i],nums[v]=nums[v],nums[i]
            else:
                i+=1
        for i in range(length):
            if i+1!=nums[i]:
                return i+1
        return length+1