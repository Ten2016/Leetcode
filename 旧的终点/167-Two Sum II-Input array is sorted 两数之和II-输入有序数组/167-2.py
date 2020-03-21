class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        p,q=0,len(numbers)-1
        while True:
            tar=numbers[p]+numbers[q]-target
            if tar==0:
                return[p+1,q+1]
            elif tar>0:
                q-=1
            else:
                p+=1