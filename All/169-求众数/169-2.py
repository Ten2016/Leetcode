class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length=len(nums)>>1
        dit={}
        for i in nums:
            if i not in dit:
                dit[i]=1
            else:
                dit[i]+=1
            if dit[i]>length:
                return i