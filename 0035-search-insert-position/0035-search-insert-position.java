class Solution {
    public int searchInsert(int[] nums, int target) {
        int index=0;
        for(int num : nums){
            if(num>=target){
                break;
            }
            index++;
        }
        return index;
    }
}