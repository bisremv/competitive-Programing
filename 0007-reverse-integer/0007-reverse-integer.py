class Solution:
    def reverse(self, x: int) -> int:
        ans=0
        if x>0:
            rev=str(x)[::-1]
            ans=int(rev)
        elif x<0:
            rev=str(x)[1:]
            ans=-int(rev[::-1])
        if ans > 2**31 or ans <-2**31-1:
            return 0
        return ans
        