class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        result=[]
        for i in range(len(sentences)):
            x=sentences[i].split()
            re=len(x)
            result.append(re)
        return max(result)
