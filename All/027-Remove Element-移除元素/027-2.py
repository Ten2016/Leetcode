class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        p=0
        for i in nums:
            if i!=val:
                nums[p]=i
                p+=1
        return p