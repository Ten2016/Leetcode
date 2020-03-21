class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        s=str(x)
        p,q=0,len(s)-1
        while p<q:
            if s[p]!=s[q]:
                return False
            p+=1
            q-=1
        return True