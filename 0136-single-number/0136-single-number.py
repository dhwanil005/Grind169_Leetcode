class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = dict(collections.Counter(nums))
        for k,v in x.items():
            if v==1:
                return k
        