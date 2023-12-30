class Solution:
    def isPalindrome(self, x: int) -> bool:
        ans=0
        temp=x
        while x > 0:
            dig=x%10
            ans=ans*10+dig
            x//=10
        return True if ans == temp  else False
        