class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        a=[]
        for i in range(len(words)):
            for j in words[i]:
                if j == x:
                    a.append(i)
                    break
        return a