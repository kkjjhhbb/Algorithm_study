class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                ans+=prices[i]-prices[i-1]
        return ans

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(prices[i+1]-prices[i],0) for i in range(len(prices)-1))
#0보다 크면 무조건 합산