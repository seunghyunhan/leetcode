"""
@author : Seunghyun
247. Strobogrammatic Number II
https://leetcode.com/problems/strobogrammatic-number-ii/
"""
import itertools

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        if n == 0:
            return [""]
        elif n == 1:
            return ["0", "1", "8"]
        
        output = []
        stro_number = [1,8,0]
        pair_number = [6,9]
        reverse_pair = {6: 9, 9: 6}
        
        candidates = stro_number + pair_number
        
        if n % 2 != 0:
            mid_term = ["1","8","0"]
        else:
            mid_term = []
        
        r = n//2
        if r == 1:
            for s in ["11", "88", "69", "96"]:
                if not mid_term:  
                    output.append(s)
                else:
                    for mid in mid_term:
                        output.append(s[0] + mid + s[1])
            
        elif r > 1:
            half_list = [p for p in itertools.product(candidates, repeat=r)]
            
            for front in half_list:
                if front[0] != 0:
                    front_term = ''.join([str(e) for e in list(front)])
                    rear_term = reversed([e for e in list(front)])
                    rear_term = [str(e) if e not in pair_number else str(reverse_pair[e]) for e in rear_term]
                    rear_term = ''.join(rear_term)
                    
                    if not mid_term:    
                        output.append(front_term + rear_term)
                    else:
                        for mid in mid_term:
                            output.append(front_term + mid + rear_term)
        
        return output
