class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=set()
        for i in nums:
            if i not in s:
                s.add(i)
            else:
                return i