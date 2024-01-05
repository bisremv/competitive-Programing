class Solution:
    def convert(self, s: str, numRows: int) -> str:
        count=0
        forward=True
        dict={}
        for i in s:
            if numRows ==1:
                return s
            if count >= numRows:
                print("Rev++++++")
                forward=False
            if count == 1 and forward==False:
                print("Frward++++++")
                forward=True
            if forward:
                count+=1
            else:
                count-=1
            if dict.get(count) !=None:
                print("add on", count)
                dict[count].append(i)
                print(dict[count])
            else:
                print("new dict",count)
                dict[count]=[i]
                print(dict[count])
        ans=[]
        for i in dict.values():
            ans.extend(i)
        return "".join(ans)          