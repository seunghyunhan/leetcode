"""
@author : Seunghyun
1055. Shortest Way to Form String
https://leetcode.com/problems/shortest-way-to-form-string/
"""

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        idx = 0
        subsequence_cnt = 0
        while idx < len(target): 
            change_detect = False
            for e in source:
                if idx < len(target) and target[idx] == e:
                    change_detect = True
                    idx += 1
            if change_detect:
                subsequence_cnt += 1
            else:
                return -1
        return subsequence_cnt
