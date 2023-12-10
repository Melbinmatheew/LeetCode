class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        stack = []
        next= {}
        for i in nums2:
            while stack and stack[-1] < i:
                next[stack.pop()] = i
            stack.append(i)
        for i in nums1:
            res.append(next.get(i, -1))
        return res