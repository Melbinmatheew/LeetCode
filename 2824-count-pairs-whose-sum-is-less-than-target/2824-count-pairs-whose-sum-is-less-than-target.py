class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        c=0
        for i in range(len(nums)-1):
            for j in range(len(nums)):
                if i<j and nums[i]+nums[j]<target:
                    c+=1
        return c