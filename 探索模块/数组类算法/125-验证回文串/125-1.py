class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p,q=0,len(s)-1
        while p<q:
            if not s[p].isalnum():
                p+=1
                continue
            elif not s[q].isalnum():
                q-=1
                continue
            if s[p].lower()!=s[q].lower():
                return False
            else:
                p+=1
                q-=1
        return True