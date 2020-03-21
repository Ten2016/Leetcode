class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        left,right=0,len(letters)-1
        while left<=right:
            mid=(left+right)>>1
            if letters[mid]==target:
                while mid<len(letters) and letters[mid]==target:
                    mid+=1
                if mid==len(letters):
                    return letters[0]
                else:
                    return letters[mid]
            elif letters[mid]<target:
                left=mid+1
            else:
                right=mid-1
        if left==len(letters):
            return letters[0]
        else:
            return letters[left]