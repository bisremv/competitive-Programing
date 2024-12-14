class Solution {
    public int removeElement(int[] nums, int val) {
      int k = 0;
      int i=0;
      for (int n : nums){
        if (n != val){
        k++;
        nums[i]=n;
        i++;
        }
      }  
      return k;    
    }
}