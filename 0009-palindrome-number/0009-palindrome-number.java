class Solution {
    public boolean isPalindrome(int x) {
   if (x < 0) return false;

        // Convert the integer to a string
        String valueString = String.valueOf(x);

        // Loop through half of the string
        for (int i = 0; i < valueString.length() / 2; i++) {
            // Compare characters from the start and end
            if (valueString.charAt(i) != valueString.charAt(valueString.length() - 1 - i)) {
                return false; // Not a palindrome
            }
        }
        return true; // It's a palindrome
    }
}