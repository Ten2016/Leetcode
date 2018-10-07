class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dit={}
        for i in nums:
            if i not in dit:
                dit[i]=1
            else:
                return True
        return False