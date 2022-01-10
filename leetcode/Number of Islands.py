class Solution:
    
    def dfs(self, grid: List[List[str]],i:int,j:int,visited) -> int:
        n=len(grid)
        m=len(grid[0])
        
        if 0 <= i < n and 0<= j < m:
            if visited[i][j]:
                return False

            if grid[i][j] == '1':
                visited[i][j]=True
                self.dfs(grid,i+1,j,visited)
                self.dfs(grid,i-1,j,visited)
                self.dfs(grid,i,j+1,visited)
                self.dfs(grid,i,j-1,visited)
                return True
            
    def numIslands(self, grid: List[List[str]]) -> int:
        n=len(grid)
        m=len(grid[0])
        visited=[[False] * m for _ in range(n)]
        ans =0

        for i in range(n):
            for j in range(m):
                if self.dfs(grid,i,j,visited):
                    ans += 1

        return ans