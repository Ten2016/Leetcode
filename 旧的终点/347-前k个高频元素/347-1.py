class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 统计个数
        dit={}
        for i in nums:
            if i not in dit:
                dit[i]=1
            else:
                dit[i]+=1
        tmp=sorted(dit.items(),key=lambda item:item[1],reverse=True)
        return [tmp[i][0] for i in range(k)]