class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        re=[]
        for i in range(0,len(nums),2):
            fre=nums[i]
            value=nums[i+1]
            re+=[value]*fre
        return re