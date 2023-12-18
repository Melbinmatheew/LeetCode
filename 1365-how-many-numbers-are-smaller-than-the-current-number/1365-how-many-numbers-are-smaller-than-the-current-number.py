class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        a=[]
        for i in nums:
            a.append(len([x for x in nums if x < i]))
        return a
            
