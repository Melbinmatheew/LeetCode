class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count=0
        m=list(jewels)
        n=list(stones)
        for i in range(len(m)):
            for j in range(len(n)):
                if m[i] in n[j]:
                    count+=1
        return count