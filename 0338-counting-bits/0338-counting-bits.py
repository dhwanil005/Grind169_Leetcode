class Solution:
    def countBits(self, n: int) -> List[int]:
        helper = []
       
        for i in range(n+1):
             
            helper.append((bin(i)))
        
        
        for i in range(len(helper)):
            helper[i] = helper[i].count("1")
        return helper