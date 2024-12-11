class Solution {
    public int removeDuplicates(int[] nums) {
       int numUniqe=1;
       int currentNum = nums[0];
       int currentindex=1;
       for (int num : nums){
        if(currentNum < num){
            nums[currentindex]=num;
            currentindex++;
            numUniqe++;
            currentNum=num;
        }
       }
       return numUniqe;     
    }
}