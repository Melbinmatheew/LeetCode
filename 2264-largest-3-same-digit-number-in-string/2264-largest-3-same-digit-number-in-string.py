class Solution:
    def largestGoodInteger(self, num: str) -> str:
        large = ''

        for i in range(len(num)-2):
            new = num[i:i+3]

            if new[0]==new[1]==new[2]:
                if new > large:
                    large = new
        return large
