"""
@author : Seunghyun
624. Maximum Distance in Arrays
https://leetcode.com/problems/maximum-distance-in-arrays/
"""
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        if len(arrays) <= 1:
            return 0
        
        min_lst = [[-1, 10001], [-1, 10001]]
        max_lst = [[-1, -10001], [-1, -10001]]
        for i, arr in enumerate(arrays):
            min_val = arr[0]
            max_val = arr[-1]
            
            if min_val < min_lst[0][1]:
                min_lst[1] = min_lst[0]
                min_lst[0] = [i, min_val]
                
            elif min_val < min_lst[1][1]:
                min_lst[1] = [i, min_val]        
            
            if max_val > max_lst[0][1]:
                max_lst[1] = max_lst[0]
                max_lst[0] = [i, max_val]
            elif max_val > max_lst[1][1]:
                max_lst[1] = [i, max_val]
        
        output = 0
        if min_lst[0][0] != max_lst[0][0]:
            output = max_lst[0][1] - min_lst[0][1]
        else:
            cand1 = max_lst[0][1] - min_lst[1][1]
            cand2 = max_lst[1][1] - min_lst[0][1]
            output = max(cand1, cand2)
        return output
