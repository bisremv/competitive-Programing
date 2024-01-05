class Solution:
    def convert(self, s: str, numRows: int) -> str:
        count=0
        forward=True
        dict={}
        for i in s:
            if numRows ==1:
                return s
            if count >= numRows:
                forward=False
            if count == 1 and forward==False:
                forward=True
            if forward:
                count+=1
            else:
                count-=1
            if dict.get(count) !=None:
                dict[count].append(i)
            else:
                dict[count]=[i]
        ans=[]
        for i in dict.values():
            ans.extend(i)
        return "".join(ans)          