class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        x = dict(collections.Counter(nums))
        for k,v in x.items():
            if v==1:
                return k
        