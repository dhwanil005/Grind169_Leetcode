class Solution:
    def hammingWeight(self, n: int) -> int:
        temp = int(n)
        return bin(temp).count("1")