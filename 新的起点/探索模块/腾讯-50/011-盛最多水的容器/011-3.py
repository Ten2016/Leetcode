class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        p,q=0,len(height)-1
        maxv=0
        while p<q:
            if height[p]<height[q]:
                minl= height[p]
                p+=1
            else:
                minl= height[q]
                q-=1
            v=minl*(q-p+1)
            if maxv<v:
                maxv=v
        return maxv