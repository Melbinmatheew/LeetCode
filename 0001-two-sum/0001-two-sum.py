class Solution(object):
    def twoSum(self, nums, target):
        self.nums=nums
        self.target=target
        h=int(len(nums))
        for i in range(h):
            for j in range(i+1,h):
                if nums[i]+nums[j]==target:
                    return [i,j]