class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        re=nums[-1]*nums[-2]*nums[-3]
        re1=nums[0]*nums[1]*nums[-1]
        return max(re,re1)