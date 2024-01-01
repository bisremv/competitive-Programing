class Solution:
    def romanToInt(self, s: str) -> int:
        ans=0
        ans2=0
        out=0
        temp=""
        for i in range(len(s)):
            ans=0
            ans2=0
            # s[i]=s[i].lower()
            if len(temp) > 0:
                temp+=s[i]
                match temp.lower():
                    case "cm":
                        ans+=900
                    case "cd":
                        ans+=400
                    case "xc":
                        ans+=90
                    case "xl":
                        ans+=40
                    case "ix":
                        ans+=9
                    case "iv":
                        ans+=4
                    case "i":
                        ans+=1
            else:
                match s[i].lower():
                    case "m":
                        ans+=1000
                    case "d":
                        ans+=500
                    case "c":
                        ans+=100
                    case "l":
                        ans+=50
                    case "x":
                        ans+=10
                    case "v":
                        ans+=5
                    case "i":
                        ans+=1
            if i < len(s)-1 and len(temp)==0:
                match s[i+1].lower():
                    case "m":
                        ans2+=1000
                    case "d":
                        ans2+=500
                    case "c":
                        ans2+=100
                    case "l":
                        ans2+=50
                    case "x":
                        ans2+=10
                    case "v":
                        ans2+=5
                    case "i":
                        ans2+=1
                if ans >= ans2:
                    out+=ans
                else:
                    temp=s[i]
            else:
                temp=""
                out+=ans
        return out
            
                
                
