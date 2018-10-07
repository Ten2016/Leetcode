class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<3:
            return len(nums)
        p,n=0,1
        for i in nums[1:]:
            if nums[p]!=i:
                p+=1
                nums[p]=i
                n=1
            else:
                if n<2:
                    p+=1
                    nums[p]=i
                    n+=1
        return p+1