class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(n):
            power=2**i or n%2==0
            if n==1:
                return True
            if power ==n:
                return True
            if power >n:
                return False