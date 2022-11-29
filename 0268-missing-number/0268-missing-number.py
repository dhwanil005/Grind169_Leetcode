class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        presentSum=n*(n+1)/2
        return int(presentSum-sum(nums))
        
        