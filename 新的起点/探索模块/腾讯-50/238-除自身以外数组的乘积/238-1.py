class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 打表记录
        l_lst,r_lst=[],[]
        length=len(nums)-1
        mux=1
        for i in nums:
            mux*=i
            l_lst.append(mux)
        mux=1
        for i in nums[::-1]:
            mux*=i
            r_lst.append(mux)
        res=[]
        res.append(r_lst[length-1])   
        for i in range(1,length):
            res.append(l_lst[i-1]*r_lst[length-i-1])
        res.append(l_lst[length-1])
        return res