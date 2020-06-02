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
        mid=0
        while left<=right:
            mid=(left+right)>>1
            if arr[mid]>=x:
                right=mid-1
            else:
                left=mid+1
        res=[]
        z,y=left-1,left
        kk=0
        while kk<k:
            if z>=0 and y<length:
                if abs(arr[z]-x)<=abs(arr[y]-x):
                    res.append(arr[z])
                    z-=1
                else:
                    res.append(arr[y])
                    y+=1
                kk+=1
            elif z<0:
                res.append(arr[y])
                y+=1
                kk+=1
            elif y>=length:
                res.append(arr[z])
                z-=1  
                kk+=1
        res.sort()
        return res
                
                