class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        re=[]
        for i in range(len(nums)):
            if nums[i] == target:
                re.append(i)
        return re