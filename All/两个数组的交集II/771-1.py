class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        dit=set()
        for i in J:
            dit.add(i)
        cnt=0
        for i in S:
            if i in dit:
                cnt+=1
        return cnt