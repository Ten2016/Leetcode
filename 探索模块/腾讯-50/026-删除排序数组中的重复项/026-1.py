class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        p=0
        for i in nums:
            if i!=nums[p]:
                p+=1
                nums[p]=i
        return p+1