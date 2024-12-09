class Solution {
    public int romanToInt(String s) {
        Map<Character, Integer> romanToInt = Map.of(
            'I', 1,
            'V', 5,
            'X', 10,
            'L', 50,
            'C', 100,
            'D', 500,
            'M', 1000
        );

        int total = 0;
        int prevValue = 0;

        // Iterate through the Roman numeral string from right to left
        for (int i = s.length() - 1; i >= 0; i--) {
            char currentChar = s.charAt(i);
            int currentValue = romanToInt.get(currentChar);

            if (currentValue < prevValue) {
                // Subtractive case
                total -= currentValue;
            } else {
                // Additive case
                total += currentValue;
            }

            prevValue = currentValue;
        }

        return total;
        }
    
}