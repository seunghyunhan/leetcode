"""
@author: Seunghyun
307. Range Sum Query - Mutable
https://leetcode.com/problems/range-sum-query-mutable/
"""
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def update(self, i: int, val: int) -> None:
        self.nums[i] = val

    def sumRange(self, i: int, j: int) -> int:
        sum_num = 0
        for e in self.nums[i:j+1]:
            sum_num += e
        return sum_num


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
