class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dit={}
        res=[]
        for i in nums1:
            if i not in dit:
                dit[i]=1
            else:
                dit[i]+=1
        for i in nums2:
            if i in dit:
                res.append(i)
                dit[i]-=1
                if dit[i]==0:
                    del dit[i]
        return res
                    