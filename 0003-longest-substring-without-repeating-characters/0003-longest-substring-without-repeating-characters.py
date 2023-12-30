class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}  # To store the last index of each character
        start = 0  # Start of the current substring
        max_length = 0  # Maximum length of substring without repeating characters

        for end in range(len(s)):
            if s[end] in char_index_map and char_index_map[s[end]] >= start:
            # If the current character is already in the substring, update the start
                start = char_index_map[s[end]] + 1

        # Update the last index of the current character
            char_index_map[s[end]] = end

        # Update the maximum length if the current substring is longer
            max_length = max(max_length, end - start + 1)

        return max_length
            
        