class Solution:
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        #找到x所在的位置
        length=len(arr)
        left,right=0,length-1
        for i in range(length-k):
            if abs(arr[left]-x)<=abs(arr[right]-x):
                right-=1
            else:
                left+=1
        return arr[left:right+1]

                
                