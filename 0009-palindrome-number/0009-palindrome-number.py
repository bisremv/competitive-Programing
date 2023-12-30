class Solution:
    def isPalindrome(self, x: int) -> bool:
        ans=0
        temp=x
        while x > 0:
            dig=x%10
            ans=ans*10+dig
            x//=10
        if ans==temp:
            return True
        else:
            return False
        