class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        x=0
        y=0
        for i in range(len(position)):
            if position[i]% 2 == 0:
                x=x+1
            else:
                y=y+1
        return min(x,y)