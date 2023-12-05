class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums=sorted(nums,reverse=True)
        new=set(nums)
        for i in range(len(nums)):
            if 0-nums[i] in new:
                return nums[i]
        return -1