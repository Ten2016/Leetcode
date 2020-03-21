class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n1,n2,n3=0,0,0
        for i in nums:
            if i==0:
                n1+=1
            elif i==1:
                n2+=1
            else:
                n3+=1
        for i in range(len(nums)):
            if i<n1:
                nums[i]=0
            elif i<n1+n2:
                nums[i]=1
            else:
                nums[i]=2