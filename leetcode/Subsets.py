class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        stack=[]
        
        def dfs(start):
            if stack not in ans:
                ans.append(stack[:])

            for i in range(start,len(nums)):
                stack.append(nums[i])
                dfs(i+1)
                stack.pop()

        for i in range(len(nums)):
            dfs(i)

        return ans