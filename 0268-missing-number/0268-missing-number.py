class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if len(nums) not in nums:
                return len(nums)
            if i not in nums:
                return i