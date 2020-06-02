class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums=nums1+nums2
        nums.sort()
        x=len(nums)
        if x%2:
            return nums[x//2]
        else:
            return (nums[x//2]+nums[x//2-1])/2
        
            