class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        res=[]
        a=[]
        b=[]
        for i in range(len(nums)):
            if nums[i] % 2 ==0:
                a.append(nums[i])
            else :
                b.append(nums[i])
        for i in range(len(a)):
            res.append(a[i])
            res.append(b[i])
        return res 
