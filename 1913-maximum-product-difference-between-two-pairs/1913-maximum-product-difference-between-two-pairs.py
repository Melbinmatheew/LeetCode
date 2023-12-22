class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        num=sorted(nums)
        re=((num[0]*num[1])-(num[-1]*num[-2]))
        return abs(re)