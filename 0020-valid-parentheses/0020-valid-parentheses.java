class Solution {
    public boolean isValid(String s) {
        String temp= "";
        for(char c:s.toCharArray()){
            if(c=='(' ||c=='{' ||c=='['){
                temp=temp+c;
            }
            else if( temp==""&&(c==']' ||c=='}' ||c==')')){
                return false;
            }
            else if(c==')'){
                if(temp.charAt(temp.length() - 1)=='('){
                temp=temp.substring(0, temp.length() - 1);
                }
                else{
                    return false;
                }
                }
            else if(c==']'){
                if(temp.charAt(temp.length() - 1)=='['){
            temp=temp.substring(0, temp.length() - 1);
                    }
                else{
                    return false;
                }
                }
            else if(c=='}'){
                if(temp.charAt(temp.length() - 1)=='{'){
                temp=temp.substring(0, temp.length() - 1);
                    }
                else{
                    return false;
                }
                }
        }
        if(temp==""){
            return true;
        }
        return false;
    }
}