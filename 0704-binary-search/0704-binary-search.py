class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        low = 0
        high = len(nums)
        
        while low < high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        
        return low