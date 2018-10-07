class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # 99.74%
        p,q=0,len(nums)-1
        while(p<=q):
            if nums[p]==val:
                nums[p]=nums[q]
                q-=1
            else:
                p+=1
        return p