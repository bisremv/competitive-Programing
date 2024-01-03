class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=int(''.join(map(str,digits)))
        num=num+1
        dig=str(num)
        ans=[]
        for i in dig:
            ans.append(int(i))
        return ans