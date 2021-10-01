class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        ans=0
        pair=[]
        nums.sort()
        for i in range(0,len(nums),2):
            ans+=nums[i]  
        return ans

#파이써닉한 방법
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
      return sum(sorted(nums)[::2])