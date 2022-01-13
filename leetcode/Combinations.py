class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        def dfs(start: int,k:int,elements):
            if k==0:
                ans.append(elements[:])

            for i in range(start,n+1):
                elements.append(i)
                dfs(i+1,k-1,elements)
                elements.pop()
        dfs(1,k,[])
        return ans