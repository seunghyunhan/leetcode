"""
@author : Seunghyun
159. Longest Substring with At Most Two Distinct Characters
https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
"""

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        max_len = 0
        for i in range(len(s)):
            char_set = set()
            tmp_len = 0
            
            for j in range(i, len(s)):
                char_set.add(s[j])
                
                if len(char_set) <= 2:
                    tmp_len += 1
                    if j == len(s)-1 and max_len < tmp_len:
                        max_len = tmp_len                    
                else:
                    if max_len < tmp_len:
                        max_len = tmp_len
                    break
                
        return max_len
