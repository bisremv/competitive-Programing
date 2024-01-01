class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans=0
        for i in words:
            val = True
            temp=list(chars)
            count=0
            for j in i:
                count+=1
                if j not in temp:
                    val=False
                else:
                    temp.remove(j)
                if count == len(i) and val == True :
                    ans+=len(i)
        return ans


