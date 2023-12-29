class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i, char_group in enumerate(zip(*strs)):
        # Check if all characters in the current group are the same
            if len(set(char_group)) == 1:
                continue
            else:
            # Found a mismatch, return the common prefix
                return strs[0][:i]

    # If all characters match up to the length of the shortest string, return that string
        return min(strs)
                    
            
            
            
            
                
        
        