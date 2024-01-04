class Solution:
    def mySqrt(self, x: int) -> int:
        ans=0
        for i in range(x+1):
            if i*i > x:
                break
            elif i*i==x:
                ans=i
            else:
                ans=i
        return ans