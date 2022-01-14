class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        stack=[]
        def dfs(start):
            if sum(stack) == target:
                if stack not in ans:
                    ans.append(stack[:])

            if sum(stack) > target:
                return

            for i in range(start,len(candidates)):
                stack.append(candidates[i])
                dfs(i)
                stack.pop()

        for i in range(len(candidates)):
            dfs(i)
            
        return ans