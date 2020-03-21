class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        queue=[]
        queue.append([n,0])
        visited = [False for i in range(n+1)]
        visited[n] = True
        while any(queue):
            num, step = queue.pop(0)
            i = 1
            tNum = num - i**2
            while tNum >= 0:
                if tNum == 0:
                    return step + 1

                if not visited[tNum]:
                    queue.append((tNum, step + 1))
                    visited[tNum] = True
                i += 1
                tNum = num - i**2