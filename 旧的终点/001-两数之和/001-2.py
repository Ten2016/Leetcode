class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """     
        # 前99.74%
        dic={}
        i=0
        for j in nums:
            sub=target-j
            if sub in dic:
                return [dic[sub],i]
            dic[j]=i
            i+=1