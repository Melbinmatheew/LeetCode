class Solution(object):
    def twoSum(self, nums, target):

        b=int(len(nums))
        for i in range(b):
            for j in range(i+1,b):
                if nums[i]+nums[j]==target:
                    return [i,j]