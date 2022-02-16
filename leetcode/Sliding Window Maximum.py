#1
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return nums
        l=len(nums)
        ans=[]
        for i in range(l-k+1):
            ans.append(max(nums[i:i+k]))
        return ans

#2
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        results=[]
        window=collections.deque()
        current_max=float('-inf')
        for i,v in enumerate(nums):
            window.append(v)
            if i<k-1:
                continue #k만큼은 로직 생각 않고 일단 넣는다
            if current_max == float('-inf'):
                current_max=max(window)
            elif v>current_max:
                current_max=v
            results.append(current_max)
            if current_max == window.popleft():
                current_max = float('-inf')
        return results

#3
class Solution:
    def maxSlidingWindow(self, nums, k):
        queue, ans = deque(), []  # queue: list of index where nums[index] is decreasing
        for i, n in enumerate(nums):
            while queue and nums[queue[-1]] < n:
            	queue.pop()
            queue.append(i)
            if queue[0] == i - k:
            	queue.popleft()
            if i >= k - 1:
            	ans.append(nums[queue[0]])

        return ans