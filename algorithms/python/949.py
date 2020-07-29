"""
@author : seunghyun
949. Largest Time for Given Digits
https://leetcode.com/problems/largest-time-for-given-digits/
"""
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        a = sorted(A)
    
        max_digits = [-1, -1, 5, 9]
        second_digits = {0: 9, 1: 9, 2: 3}
        
        init_candidates = []
        for elem in a:
            if elem <= 2:
                init_candidates.append(elem)
               
        output = ""
        while init_candidates:
            a_copy = a.copy()
            # print (init_candidates)
            
            output = ""
            init_digit = init_candidates.pop()
            max_digits[0] = init_digit
            
            for i, threshold in enumerate(max_digits):
                candidates = list()
                for elem in a_copy:
                    if elem <= threshold:
                        candidates.append(elem)
                    else:
                        break
                if not candidates:
                    break
                    
                d = candidates[-1]
                a_copy.remove(d)

                # print (d, a_copy)
                if i == 0: # init digit
                    init_digit = d
                    max_digits[1] = second_digits[init_digit]
                elif i == 2:
                    output += ":"
                output += str(d)
            
            if len(output) == 5:
                break
        
        if len(output) != 5:
            output = ""    
            
        return output
