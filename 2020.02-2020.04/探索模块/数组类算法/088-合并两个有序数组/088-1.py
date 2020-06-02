class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        j=-1
        for i in range(m-1,-1,-1):
            nums1[j]=nums1[i]
            j-=1
        lenm=len(nums1)
        i,j,k=lenm-m,0,0
        while i<lenm and j<n:
            if nums1[i]<=nums2[j]:
                nums1[k]=nums1[i]
                i+=1
                k+=1
            else:
                nums1[k]=nums2[j]
                j+=1
                k+=1
        while i<lenm:
            nums1[k]=nums1[i]
            k+=1
            i+=1
        while j<n:
            nums1[k]=nums2[j]
            k+=1
            j+=1
