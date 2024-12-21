class Solution {
    public int lengthOfLastWord(String s) {
    s=s.trim();
    int index=s.lastIndexOf(' ');
    String siz =s.substring(index+1);
    int i=siz.length();
    return i;
    }
}