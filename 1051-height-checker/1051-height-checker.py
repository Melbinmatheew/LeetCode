class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        a=[]
        h1=sorted(heights)
        for i in range(len(heights)):
            if heights[i]!=h1[i]:
                a.append(heights[i])
        return len(a)

