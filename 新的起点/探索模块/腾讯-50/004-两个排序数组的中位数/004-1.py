class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        rlist=nums1+nums2
        rlist.sort()
        nlen = len(rlist)
        if nlen%2==0:
            return (rlist[int(nlen/2-1)]+rlist[int(nlen/2)])/2
        else:
            return rlist[int((nlen-1)/2)]