class Solution {
    public String longestCommonPrefix(String[] strs) {
        Arrays.sort(strs);
        String first=strs[0];
        String last=strs[strs.length - 1];
        int minLength = Math.min(first.length(), last.length());
        int i=0;
        while(i < minLength){
            if(first.charAt(i) == last.charAt(i)){
            i++;
            }
            else{
                break;
            }
        }
        return first.substring(0, i);
    }
}