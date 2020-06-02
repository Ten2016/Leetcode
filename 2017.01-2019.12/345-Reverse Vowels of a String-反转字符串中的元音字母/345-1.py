class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        p,q=0,len(s)-1
        lst=list(s)
        dit={'a':0,'e':0,'i':0,'o':0,'u':0}
        while p<q:
            if s[p].lower() in dit:
                if s[q].lower() in dit:
                    lst[p],lst[q]=lst[q],lst[p]
                    p+=1
                    q-=1
                else:
                    q-=1
            else:
                p+=1
        return ''.join(lst)