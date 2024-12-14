class Solution {
    public int removeElement(int[] nums, int val) {
          int k = 0; // Tracks the count of elements not equal to val
        
        // Iterate over the array
        for (int i = 0; i < nums.length; i++) {
            // If the current element is not equal to val
            if (nums[i] != val) {
                nums[k] = nums[i]; // Move the element to the position k
                k++; // Increment k
            }
        }
        
        return k; // k is the count of elements not equal to val
    }
}