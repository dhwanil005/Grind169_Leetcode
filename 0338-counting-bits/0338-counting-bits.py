class Solution:
    def countBits(self, n: int) -> List[int]:
        helper = []
       
        for i in range(n+1):
            temp = (bin(i))
            helper.append(temp[2:])
        
        
        for i in range(len(helper)):
            helper[i] = helper[i].count("1")
        return helper