class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l=[]
        l2=[]
        for i in s:
            l.append(i)
        for i in t:
            l2.append(i)
        l.sort()
        l2.sort()
        if len(l) != len(l2):
            return False
        for i in range(len(l)):
            if l[i] != l2[i]:
                return False
        return True
                
            
        