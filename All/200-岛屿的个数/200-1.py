class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        # 建立简单队列
        queue=[]
        #
        m=len(grid)     # 行
        n=len(grid[0])  # 列
        visit=[[0 for j in range(n)] for i in range(m)]
        res=0

        # 遍历grid数组
        for i in range(m):
            for j in range(n):
                # grid为1并且未被访问过
                if grid[i][j]=='1' and not visit[i][j]:
                    res+=1
                    queue.clear()
                    front=rear=-1
                    queue.append(i*n+j)
                    rear+=1
                    visit[i][j]=1
                    # 将聚在一起的1通通标记
                    while front!=rear:
                        # 将当前点出队
                        front+=1
                        xi=queue[front]//n
                        xj=queue[front]-xi*n
                        # 上面
                        if xi-1>=0 and not visit[xi-1][xj] and grid[xi-1][xj]=='1':
                            visit[xi-1][xj]=1
                            queue.append((xi-1)*n+xj)
                            rear+=1
                        # 下面
                        if xi+1<m and not visit[xi+1][xj] and grid[xi+1][xj]=='1':
                            visit[xi+1][xj]=1
                            queue.append((xi+1)*n+xj)
                            rear+=1
                        # 左面
                        if xj-1>=0 and not visit[xi][xj-1] and grid[xi][xj-1]=='1':
                            visit[xi][xj-1]=1
                            queue.append(xi*n+xj-1)
                            rear+=1
                        # 右面
                        if xj+1<n and not visit[xi][xj+1] and grid[xi][xj+1]=='1':
                            visit[xi][xj+1]=1
                            queue.append(xi*n+xj+1)
                            rear+=1
        
        return res