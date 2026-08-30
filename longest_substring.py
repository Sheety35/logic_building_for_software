class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        num = 0
        for i in range(len(s)):
            current = ""
            for j in range(i, len(s)):
                if s[j] in current:
                    break
                
                current +=s[j]
                if len(current)> num:
                    num = len(current)
    
        return num