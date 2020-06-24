class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) <= 1:
            return True
        
        ret_val = True
        intervals_sorted = sorted(intervals, key=lambda x: x[0])
        
        prev_elem = [-1,-1]
        for elem in intervals_sorted:
            if elem[0] >= prev_elem[0] and elem[0] < prev_elem[1]:
                ret_val = False
                break
            prev_elem = elem
        
        return ret_val
