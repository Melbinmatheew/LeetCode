class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        j=0
        re=[]
        for i in range(len(nums)):
           j= nums[i] + j
           re.append(j)
        return re